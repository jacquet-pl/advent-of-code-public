#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	[0-9]+
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = (
		int(match[0])
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = 0
	p2 = 0
	
	for age in puzzle_input:
		p1 += (1421, 1401, 1191, 1154, 1034, 950, 905, 779, 768, )[age]
		p2 += (6703087164, 6206821033, 5617089148, 5217223242, 4726100874, 4368232009, 3989468462, 3649885552, 3369186778, )[age]
	
	return p1, p2
