#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2015, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re
from itertools import permutations, pairwise

finditer = re.compile(BR'''(?x)
	(?P<location_L>[A-Za-z]+)
	\040\164\157\040
	(?P<location_R>[A-Za-z]+)
	\040\075\040
	(?P<distance>[0-9]+)
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = (
		(
			match['location_L'],
			match['location_R'],
			int(match['distance']),
		)
		for match in finditer(raw_puzzle_input)
	)
	
	locations = set()
	distances = dict()
	
	for location_L, location_R, distance in puzzle_input:
		locations.add(location_L)
		locations.add(location_R)
		distances[location_L, location_R] = distance
		distances[location_R, location_L] = distance
	
	route_lengths = list(
		sum(
			distances[location_L, location_R]
			for location_L, location_R in pairwise(route)
		)
		for route in permutations(locations)
	)
	
	p1 = min(route_lengths)
	p2 = max(route_lengths)
	
	return p1, p2
