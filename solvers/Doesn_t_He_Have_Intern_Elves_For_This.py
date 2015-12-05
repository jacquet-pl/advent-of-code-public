#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2015, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	[a-z]+
''').finditer

search_p1_a = re.compile(BR'''[aeiou][^aeiou]*[aeiou][^aeiou]*[aeiou]''').search
search_p1_b = re.compile(BR'''(?P<letter>[a-z])(?P=letter)''').search
search_p1_c = re.compile(BR'''(?:ab|cd|pq|xy)''').search
search_p2_a = re.compile(BR'''(?P<letters>[a-z]{2})[a-z]*(?P=letters)''').search
search_p2_b = re.compile(BR'''(?P<letter>[a-z])(?!(?P=letter))[a-z](?P=letter)''').search

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		match[0]
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = 0
	p2 = 0
	
	for string in puzzle_input:
		if search_p1_a(string) and search_p1_b(string) and not search_p1_c(string):
			p1 += 1
		if search_p2_a(string) and search_p2_b(string):
			p2 += 1
	
	return p1, p2
