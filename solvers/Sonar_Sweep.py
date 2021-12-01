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
	
	p1 = -1
	p2 = -3
	
	a, b, c = -1, -1, -1
	for d in puzzle_input:
		if c < d:
			p1 += 1
		if a < d:
			p2 += 1
		
		a, b, c = b, c, d
	
	return p1, p2
