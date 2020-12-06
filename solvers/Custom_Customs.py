#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2020, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer_a = re.compile(BR'''(?x)
	([a-z]+\012)+
''').finditer
finditer_b = re.compile(BR'''(?x)
	[a-z]+
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		tuple(
			frozenset(match_b[0])
			for match_b in finditer_b(match_a[0])
		)
		for match_a in finditer_a(raw_puzzle_input)
	)
	
	p1 = sum(
		len(frozenset.union(*forms))
		for forms in puzzle_input
	)
	
	p2 = sum(
		len(frozenset.intersection(*forms))
		for forms in puzzle_input
	)
	
	return p1, p2
