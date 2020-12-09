#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2020, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import itertools
import re

finditer = re.compile(BR'''(?x)
	[0-9]+
''').finditer

preamble_length = 25

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		int(match[0])
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = next(
		puzzle_input[index]
		for index in range(preamble_length, len(puzzle_input))
		if puzzle_input[index] not in map(
			sum,
			itertools.combinations(
				puzzle_input[index-preamble_length:index],
				2
			)
		)
	)
	
	contiguous_set = next(
		puzzle_input[index:index +size +1]
		for index in range(len(puzzle_input))
		for size, total in enumerate(
			itertools.takewhile(
				lambda total: total <= p1,
				itertools.accumulate(
					puzzle_input[index:]
				)
			)
		)
		if p1 == total
	)
	
	p2 = min(contiguous_set) + max(contiguous_set)
	
	return p1, p2
