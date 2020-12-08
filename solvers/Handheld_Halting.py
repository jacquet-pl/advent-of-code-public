#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2020, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	(?P<operation>acc|jmp|nop)
	\040
	(?P<argument>[\053\055][0-9]+)
''').finditer

def run(instructions: list[tuple[bytes, int]]):
	instruction_pointer = 0
	touched: set[int] = set()
	accumulator = 0
	
	while instruction_pointer not in touched and instruction_pointer < len(instructions):
		touched.add(instruction_pointer)
		
		match instructions[instruction_pointer]:
			case B'acc', argument:
				instruction_pointer += 1
				accumulator += argument
			case B'jmp', argument:
				instruction_pointer += argument
			case B'nop', argument:
				instruction_pointer += 1
	
	return (
		instruction_pointer in touched,
		accumulator,
	)

def corrupt(instructions: list[tuple[bytes, int]], index: int):	
	corrupted = instructions.copy()
	
	match corrupted[index]:
		case B'acc', argument:
			pass
		case B'jmp', argument:
			corrupted[index] = B'nop', argument
		case B'nop', argument:
			corrupted[index] = B'jmp', argument
	
	return corrupted

def main(raw_puzzle_input: bytes):
	puzzle_input = [
		(
			match['operation'],
			int(match['argument']),
		)
		for match in finditer(raw_puzzle_input)
	]
	
	_, p1 = run(puzzle_input)
	
	_, p2 = min(
		run(corrupt(puzzle_input, index))
		for index in range(len(puzzle_input))
	)
	
	return p1, p2
