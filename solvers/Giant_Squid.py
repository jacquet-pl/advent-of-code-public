#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer_a = re.compile(BR'''(?x)
	[0-9][0-9]?(?:\054[0-9][0-9]?)+
	|
	[\0400-9][0-9](?:[\012\040][\0400-9][0-9])+
''').finditer
finditer_b = re.compile(BR'''(?x)
	[0-9]+
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = (
		(
			int(match_b[0])
			for match_b in finditer_b(match_a[0])
		)
		for match_a in finditer_a(raw_puzzle_input)
	)
	
	p1 = -1
	p2 = -1
	
	numbers, *boards = puzzle_input
	
	from collections import defaultdict
	number_to_boardrowcolumn: defaultdict[int, set[tuple[int, int, int, ]]] = defaultdict(set)
	boardrow_to_completeness: defaultdict[tuple[int, int, ], int] = defaultdict(int)
	boardcolumn_to_completeness: defaultdict[tuple[int, int, ], int] = defaultdict(int)
	board_to_numbers: list[set[int]] = list()
	complete_boards: set[int] = set()
	
	for index, board in enumerate(boards):
		board_numbers = set()
		for row in range(5):
			for column in range(5):
				number = next(board)
				number_to_boardrowcolumn[number].add((index, row, column, ))
				board_numbers.add(number)
		board_to_numbers.append(board_numbers)
	
	for number in numbers:
		for board, row, column in number_to_boardrowcolumn[number]:
			if board in complete_boards:
				pass
			elif 4 <= boardrow_to_completeness[(board, row, )] or 4 <= boardcolumn_to_completeness[(board, column, )]:
				score = (sum(board_to_numbers[board]) -number) *number
				if p1 < 0:
					p1 = score
				p2 = score
				complete_boards.add(board)
			else:
				boardrow_to_completeness[(board, row, )] += 1
				boardcolumn_to_completeness[(board, column, )] += 1
				board_to_numbers[board].remove(number)
	
	return p1, p2
