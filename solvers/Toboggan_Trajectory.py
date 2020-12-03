#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2020, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import math

def main(raw_puzzle_input: bytes):
	puzzle_input = frozenset(
		(x, y, )
		for y, line in enumerate(raw_puzzle_input.split(B'\012'))
		for x, byte in enumerate(line)
		if 35 == byte
	)
	
	width = max(x for x, y in puzzle_input) +1
	height = max(y for x, y in puzzle_input) +1
	
	encounter_count_by_slope = {
		Δ: len(
			puzzle_input.intersection(
				(
					(z *Δ[0] %width),
					(z *Δ[1]),
				)
				for z in range(height)
			)
		)
		for Δ in (
			(1, 1, ),
			(3, 1, ),
			(5, 1, ),
			(7, 1, ),
			(1, 2, ),
		)
	}
	
	p1 = encounter_count_by_slope[(3, 1, )]
	p2 = math.prod(encounter_count_by_slope.values())
	
	return p1, p2
