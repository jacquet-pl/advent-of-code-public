#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re
import collections

finditer = re.compile(BR'''(?x)
	(?P<x1>[0-9]+)
	\054
	(?P<y1>[0-9]+)
	\040\055\076\040
	(?P<x2>[0-9]+)
	\054
	(?P<y2>[0-9]+)
''').finditer

def main(raw_puzzle_input: bytes):
	puzzle_input = (
		(
			int(match['x1']),
			int(match['y1']),
			int(match['x2']),
			int(match['y2']),
		)
		for match in finditer(raw_puzzle_input)
	)
	
	hits1 = collections.defaultdict(int)
	hits2 = collections.defaultdict(int)
	for x1, y1, x2, y2 in puzzle_input:
		if x1 < x2:
			δx = 1
		elif x2 < x1:
			δx = -1
		else:
			δx = 0
		
		if y1 < y2:
			δy = 1
		elif y2 < y1:
			δy = -1
		else:
			δy = 0
		
		if 0 == δx or 0 == δy:
			hits1[x1, y1, ] += 1
			hits2[x1, y1, ] += 1
			while not (x1 == x2 and y1 == y2):
				x1 += δx
				y1 += δy
				hits1[x1, y1, ] += 1
				hits2[x1, y1, ] += 1
		else:
			hits2[x1, y1, ] += 1
			while not (x1 == x2 and y1 == y2):
				x1 += δx
				y1 += δy
				hits2[x1, y1, ] += 1
	
	p1 = sum(
		1
		for v in hits1.values()
		if 1 < v
	)
	p2 = sum(
		1
		for v in hits2.values()
		if 1 < v
	)
	
	return p1, p2
