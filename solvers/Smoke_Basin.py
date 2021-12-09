#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	[0-9]+
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = {
		(x, y): z -47
		for y, match in enumerate(finditer(raw_puzzle_input))
		for x, z in enumerate(match[0])
	}
	
	low_xy = {
		(x, y): z
		for (x, y), z in puzzle_input.items()
		if z < puzzle_input.get((x +1, y, ), 99)
		if z < puzzle_input.get((x -1, y, ), 99)
		if z < puzzle_input.get((x, y +1, ), 99)
		if z < puzzle_input.get((x, y -1, ), 99)
	}
	
	p1 = sum(low_xy.values())
	
	sizes = list()
	for x, y in low_xy.keys():
		openset: set[tuple[int, int]] = set()
		seen: set[tuple[int, int]] = set()
		openset.add((x, y, ))
		
		while openset:
			x, y = openset.pop()
			if 10 == puzzle_input.get((x, y, ), 10):
				pass
			elif (x, y, ) in seen:
				pass
			else:
				seen.add((x, y, ))
				openset.add((x +1, y, ))
				openset.add((x -1, y, ))
				openset.add((x, y +1, ))
				openset.add((x, y -1, ))
		
		sizes.append(len(seen))
	
	from math import prod
	p2 = prod(sorted(sizes)[-3:])
	
	return p1, p2
