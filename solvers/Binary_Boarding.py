#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2020, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	[BF]{7}
	[RL]{3}
''').finditer

table = bytes.maketrans(B'BFRL', B'1010')

def main(raw_puzzle_input: bytes):
	puzzle_input = sorted(
		int(match[0].translate(table), base=2)
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = -3
	p2 = 0
	
	for seat in puzzle_input:
		if p1 +2 == seat:
			p2 = p1 +1
		
		p1 = seat
	
	return p1, p2
