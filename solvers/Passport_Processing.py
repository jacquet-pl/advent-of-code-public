#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2020, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re

finditer_a = re.compile(BR'''(?x)
	(?:
		(?:byr|iyr|eyr|hgt|hcl|ecl|pid|cid)
		\072
		[^\012\040]*
		[\012\040]
	)+
''').finditer
finditer_b = re.compile(BR'''(?x)
	(?:byr|iyr|eyr|hgt|hcl|ecl|pid|cid)
	\072
	[^\012\040]*
''').finditer
fullmatch = re.compile(BR'''(?x)
	|byr\07219[2-9][0-9]
	|byr\072200[0-2]
	
	|iyr\072201[0-9]
	|iyr\0722020
	
	|eyr\072202[0-9]
	|eyr\0722030
	
	|hgt\0721[5-8][0-9]cm
	|hgt\07219[0-3]cm
	|hgt\07259in
	|hgt\0726[0-9]in
	|hgt\0727[0-6]in
	
	|hcl\072\043[0-9a-f]{6}
	
	|ecl\072amb
	|ecl\072blu
	|ecl\072brn
	|ecl\072gry
	|ecl\072grn
	|ecl\072hzl
	|ecl\072oth
	
	|pid\072[0-9]{9}
	
	|cid\072[^\012\040]*
''').fullmatch

required_fields = frozenset((
	B'byr',
	B'iyr',
	B'eyr',
	B'hgt',
	B'hcl',
	B'ecl',
	B'pid',
))

def main(raw_puzzle_input: bytes):
	puzzle_input = (
		tuple(
			match_b[0]
			for match_b in finditer_b(match_a[0])
		)
		for match_a in finditer_a(raw_puzzle_input)
	)
	
	semi_valid_passports = tuple(
		passport
		for passport in puzzle_input
		if required_fields <= frozenset(
			line[0:3]
			for line in passport
		)
	)
	
	valid_passports = tuple(
		passport
		for passport in semi_valid_passports
		if all(
			fullmatch(line)
			for line in passport
		)
	)
	
	p1 = len(semi_valid_passports)
	p2 = len(valid_passports)
	
	return p1, p2
