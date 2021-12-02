#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	(?P<command>forward|down|up)
	\040
	(?P<units>[0-9]+)
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = (
		(match['command'], int(match['units']), )
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = 0
	p2 = 0
	
	horizontal_position = 0
	for command, units in puzzle_input:
		match command:
			case B'forward':
				horizontal_position += units
				p2 += p1 *units
			case B'down':
				p1 += units
			case B'up':
				p1 -= units
	
	p1 *= horizontal_position
	p2 *= horizontal_position
	
	return p1, p2
