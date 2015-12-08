#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2015, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''[^\012]+''').finditer
sub1 = re.compile(BR'''(?:\134\042|\134\134|\134\170[0-9a-f][0-9a-f])''').sub
sub2 = re.compile(BR'''[\134\042]''').sub

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		match[0]
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = 0
	p2 = 0
	
	for line in puzzle_input:
		p1 += len(line) - len(sub1(b'\000', line)) + 2
		p2 += len(sub2(b'\000\000', line)) - len(line) + 2
	
	return p1, p2
