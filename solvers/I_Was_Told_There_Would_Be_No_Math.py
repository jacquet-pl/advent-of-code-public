#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2015, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer = re.compile(BR'''(?x)
	(?P<l>[0-9]+)
	x
	(?P<w>[0-9]+)
	x
	(?P<h>[0-9]+)
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = tuple(
		(
			int(match['l']),
			int(match['w']),
			int(match['h']),
		)
		for match in finditer(raw_puzzle_input)
	)
	
	p1 = 0
	p2 = 0
	
	for length, width, height in puzzle_input:
		p1 += 2*length*width + 2*width*height + 2*height*length
		p2 += 2*length + 2*width + 2*height + length*width*height
		
		if length < width:
			if height < width:
				p1 += height*length
				p2 -= 2*width
			else:
				p1 += length*width
				p2 -= 2*height
		else:
			if length < height:
				p1 += length*width
				p2 -= 2*height
			else:
				p1 += width*height
				p2 -= 2*length
	
	return p1, p2
