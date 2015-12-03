#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2015, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	[\074\076\136\166]
''').finditer



def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		{
			b'\074': -1,
			b'\076': 1,
			b'\136': 1J,
			b'\166': -1J,
		}[match[0]]
		for match in finditer(raw_puzzle_input)
	)
	
	all = 0
	odd = 0
	even = 0
	all_visited = {0, }
	some_visited = {0, }
	
	for direction in puzzle_input:
		all += direction
		all_visited.add(all)
		
		odd += direction
		some_visited.add(odd)
		odd, even = even, odd
	
	p1 = len(all_visited)
	p2 = len(some_visited)
	
	return p1, p2
