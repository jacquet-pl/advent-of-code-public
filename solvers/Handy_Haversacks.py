#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2020, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import graphlib
import re

finditer_a = re.compile(BR'''(?x)
	(?P<color>
		[a-z]+\040[a-z]+
	)
	\040bags\040contain
	\040
	(?P<bags>
		[1-9]\040[a-z]+\040[a-z]+\040bags?
		(?:
			\054\040
			[1-9]\040[a-z]+\040[a-z]+\040bags?
		)*
		|no\040other\040bags
	)
	\056
''').finditer
finditer_b = re.compile(BR'''(?x)
	(?P<count>[1-9])
	\040
	(?P<color>[a-z]+\040[a-z]+)
	\040bags?
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input: dict[bytes, dict[bytes, int]] = {
		match_a['color']: {
			match_b['color']: int(match_b['count'])
			for match_b in finditer_b(match_a['bags'])
		}
		for match_a in finditer_a(raw_puzzle_input)
	}
	
	order = tuple(graphlib.TopologicalSorter(puzzle_input).static_order())
	
	can_contain: set[bytes] = set()
	bag_count = {
		color: 0
		for color in order
	}
	
	can_contain.add(B'shiny gold')
	bag_count[B'shiny gold'] += 1
	
	for color in order:
		if can_contain.intersection(puzzle_input[color].keys()):
			can_contain.add(color)
	
	for parent_color in reversed(order):
		for color, count in puzzle_input[parent_color].items():
			bag_count[color] += count * bag_count[parent_color]
	
	p1 = len(can_contain) -1
	p2 = sum(bag_count.values()) -1
	
	return p1, p2
