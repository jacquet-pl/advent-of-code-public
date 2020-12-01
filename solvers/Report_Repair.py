#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2020, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import itertools
import math
import re

finditer = re.compile(BR'''(?x)
	[0-9]+
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		int(match[0])
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = next(
		math.prod(combination)
		for combination in itertools.combinations(puzzle_input, 2)
		if 2020 == sum(combination)
	)
	
	p2 = next(
		math.prod(combination)
		for combination in itertools.combinations(puzzle_input, 3)
		if 2020 == sum(combination)
	)
	
	return p1, p2
