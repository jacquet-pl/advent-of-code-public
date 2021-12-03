#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	[01]+
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		tuple(match[0])
		for match in finditer(raw_puzzle_input)
	)
	
	gamma_rate = 0
	epsilon_rate = 0
	for bits in zip(*puzzle_input):
		count_0 = 0
		count_1 = 0
		for bit in bits:
			if 48 == bit:
				count_0 += 1
			else:
				count_1 += 1
		
		gamma_rate <<= 1
		epsilon_rate <<= 1
		if count_0 < count_1:
			gamma_rate |= 1
		else:
			epsilon_rate |= 1
	
	p1 = gamma_rate * epsilon_rate
	
	oxygen_generator_rating = 0
	CO2_scrubber_rating = 0
	
	selected = list(puzzle_input)
	current_bit_position = 0
	while 1 < len(selected):
		is_0 = list()
		is_1 = list()
		for value in selected:
			if 48 == value[current_bit_position]:
				is_0.append(value)
			else:
				is_1.append(value)
		
		if len(is_1) < len(is_0):
			selected = is_0
		else:
			selected = is_1
		
		current_bit_position += 1
	oxygen_generator_rating = int(bytes(selected[0]), base=2)
	
	selected = list(puzzle_input)
	current_bit_position = 0
	while 1 < len(selected):
		is_0 = list()
		is_1 = list()
		for value in selected:
			if 48 == value[current_bit_position]:
				is_0.append(value)
			else:
				is_1.append(value)
		
		if len(is_1) < len(is_0):
			selected = is_1
		else:
			selected = is_0
		
		current_bit_position += 1
	CO2_scrubber_rating = int(bytes(selected[0]), base=2)
	
	p2 = oxygen_generator_rating * CO2_scrubber_rating
	
	return p1, p2
