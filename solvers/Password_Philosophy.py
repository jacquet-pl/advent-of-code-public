#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2020, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	(?P<lo>[0-9]+)
	\055
	(?P<hi>[0-9]+)
	\040
	(?P<letter>[a-z])
	\072\040
	(?P<password>[a-z]+)
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = (
		(
			int(match['lo']),
			int(match['hi']),
			match['letter'][0],
			match['password'],
		)
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = 0
	p2 = 0
	
	for lo, hi, letter, password in puzzle_input:
		if lo <= password.count(letter) <= hi:
			p1 += 1
		if letter == password[lo -1] and letter != password[hi -1]:
			p2 += 1
		if letter != password[lo -1] and letter == password[hi -1]:
			p2 += 1
	
	return p1, p2
