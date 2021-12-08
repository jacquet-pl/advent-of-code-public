#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re
import itertools

finditer = re.compile(BR'''(?x)
	([a-g\040]+)
	\040\|\040
	([a-g\040]+)
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		(tuple(match[1].split(B'\040')), tuple(match[2].split(B'\040')), )
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = sum(
		1
		for x, ys in puzzle_input
		for y in ys
		if len(y) in (
			2, #1
			4, #4
			3, #7
			7, #8
		)
	)
	
	p2 = 0
	for xs, ys in puzzle_input:
		for a, b, c, d, e, f, g in itertools.permutations(range(7)):
			digits = {
				frozenset((a, b, c, e, f, g, )): 0,
				frozenset((c, f, )): 1,
				frozenset((a, c, d, e, g, )): 2,
				frozenset((a, c, d, f, g, )): 3,
				frozenset((b, c, d, f, )): 4,
				frozenset((a, b, d, f, g, )): 5,
				frozenset((a, b, d, e, f, g, )): 6,
				frozenset((a, c, f, )): 7,
				frozenset((a, b, c, d, e, f, g, )): 8,
				frozenset((a, b, c, d, f, g, )): 9,
			}
			
			if all(
				frozenset(line - ord('a') for line in z) in digits
				for z in (*xs, *ys, )
			):
				value = 0
				for y in ys:
					key = frozenset(line - ord('a') for line in y)
					value *= 10
					value += digits[key]
				p2 += value
				break
	
	return p1, p2
