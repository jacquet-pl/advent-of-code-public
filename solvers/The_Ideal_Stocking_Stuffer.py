#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2015, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re
import hashlib

search = re.compile(BR'''(?x)
	[a-z]+
''').search

def main(raw_puzzle_input: bytes):
	puzzle_input = (search(raw_puzzle_input) or [b'', ])[0]
	
	p1 = -1
	p2 = -1
	
	counter = 0
	
	while p2 < 0:
		counter += 1
		hash = hashlib.new('md5', puzzle_input + str(counter).encode(encoding='utf-8'), usedforsecurity=False).hexdigest()
		
		if p1 < 0 and hash.startswith('00000'):
			p1 = counter
		if p2 < 0 and hash.startswith('000000'):
			p2 = counter
	
	
	return p1, p2
