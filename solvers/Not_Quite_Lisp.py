#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2015, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	[\050\051]
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		b'\050' == match[0]
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = 0
	p2 = -1
	
	for instruction in puzzle_input:
		if instruction:
			p1 += 1
		else:
			p1 -= 1
		
		if p2 < 0:
			if p1 < 0:
				p2 = -p2
			else:
				p2 -= 1
	
	return p1, p2
