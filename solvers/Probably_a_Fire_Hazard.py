#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2015, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	(?P<action>turn\040on|turn\040off|toggle)
	\040(?P<a>[0-9]+)
	\054(?P<b>[0-9]+)
	\040through
	\040(?P<c>[0-9]+)
	\054(?P<d>[0-9]+)
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		(
			match['action'],
			int(match['a']),
			int(match['b']),
			int(match['c']),
			int(match['d']),
		)
		for match in finditer(raw_puzzle_input)
	)
	
	lit = set()
	brightness = [0, ] *1000 *1000
	
	for action, a, b, c, d in puzzle_input:
		if b'turn on' == action:
			lit |= {
				1000 *y +x
				for y in range(a, c+1)
				for x in range(b, d+1)
			}
			for y in range(a, c+1):
				for x in range(b, d+1):
					brightness[1000 *y +x] += 1
		elif b'turn off' == action:
			lit -= {
				1000 *y +x
				for y in range(a, c+1)
				for x in range(b, d+1)
			}
			for y in range(a, c+1):
				for x in range(b, d+1):
					brightness[1000 *y +x] = (
						0
						if 0 == brightness[1000 *y +x] else
						brightness[1000 *y +x] - 1
					)
		elif b'toggle' == action:
			lit ^= {
				1000 *y +x
				for y in range(a, c+1)
				for x in range(b, d+1)
			}
			for y in range(a, c+1):
				for x in range(b, d+1):
					brightness[1000 *y +x] += 2
	
	p1 = len(lit)
	p2 = sum(brightness)
	
	return p1, p2
