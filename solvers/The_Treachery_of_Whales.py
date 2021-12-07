#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	[0-9]+
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		int(match[0])
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = min(
		sum(
			abs(target - crab)
			for crab in puzzle_input
		)
		for target in range(min(puzzle_input), max(puzzle_input))
	)
	p2 = min(
		sum(
			(abs(target - crab) * (abs(target - crab) +1)) //2
			for crab in puzzle_input
		)
		for target in range(min(puzzle_input), max(puzzle_input))
	)
	
	return p1, p2
