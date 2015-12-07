#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2015, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import re
from typing import Literal, TypedDict
from operator import __or__, __and__, __lshift__, __rshift__, __invert__

finditer = re.compile(BR'''(?x)
	(?:
		(?P<or_lhs>[0-9a-z]+)\x20OR\x20(?P<or_rhs>[0-9a-z]+)|
		(?P<and_lhs>[0-9a-z]+)\x20AND\x20(?P<and_rhs>[0-9a-z]+)|
		(?P<lshift_lhs>[0-9a-z]+)\x20LSHIFT\x20(?P<lshift_rhs>[0-9]+)|
		(?P<rshift_lhs>[0-9a-z]+)\x20RSHIFT\x20(?P<rshift_rhs>[0-9]+)|
		NOT\x20(?P<not>[0-9a-z]+)|
		(?P<eq>[0-9a-z]+)
	)
	\x20\x2D\x3E\x20
	(?P<output>[a-z]+)
''').finditer

class Gate_or(TypedDict):
	opcode: Literal["__or__"]
	lhs: bytes
	rhs: bytes
class Gate_and(TypedDict):
	opcode: Literal["__and__"]
	lhs: bytes
	rhs: bytes
class Gate_lshift(TypedDict):
	opcode: Literal["__lshift__"]
	lhs: bytes
	rhs: bytes
class Gate_rshift(TypedDict):
	opcode: Literal["__rshift__"]
	lhs: bytes
	rhs: bytes
class Gate_invert(TypedDict):
	opcode: Literal["__invert__"]
	input: bytes
class Gate_eq(TypedDict):
	opcode: Literal["__eq__"]
	input: bytes
Gates = dict[bytes, Gate_or | Gate_and | Gate_lshift | Gate_rshift | Gate_invert | Gate_eq]

def resolve(key: bytes, gates: Gates, memory: dict[bytes, int]) -> int:
	if key.isdigit():
		return int(key)
	
	if key in memory:
		return memory[key]
	
	match gates[key]:
		case {"opcode": "__or__", "lhs": lhs, "rhs": rhs, }:
			value = resolve(lhs, gates, memory) | resolve(rhs, gates, memory)
		case {"opcode": "__and__", "lhs": lhs, "rhs": rhs, }:
			value = resolve(lhs, gates, memory) & resolve(rhs, gates, memory)
		case {"opcode": "__lshift__", "lhs": lhs, "rhs": rhs, }:
			value = resolve(lhs, gates, memory) << resolve(rhs, gates, memory)
		case {"opcode": "__rshift__", "lhs": lhs, "rhs": rhs, }:
			value = resolve(lhs, gates, memory) >> resolve(rhs, gates, memory)
		case {"opcode": "__invert__", "input": input, }:
			value = ~resolve(input, gates, memory)
		case {"opcode": "__eq__", "input": input, }:
			value = resolve(input, gates, memory)
		case _:
			value = 0
	
	memory[key] = value
	
	return value

def main(raw_puzzle_input: bytes):
	puzzle_input = (
		match
		for match in finditer(raw_puzzle_input)
	)
	
	gates: Gates = dict()
	for raw_gate in puzzle_input:
		match raw_gate.groupdict():
			case {"output": output, "or_lhs": lhs, "or_rhs": rhs, } if lhs is not None:
				gates[output] = {
					"opcode": "__or__",
					"lhs": lhs,
					"rhs": rhs,
				}
			case {"output": output, "and_lhs": lhs, "and_rhs": rhs, } if lhs is not None:
				gates[output] = {
					"opcode": "__and__",
					"lhs": lhs,
					"rhs": rhs,
				}
			case {"output": output, "lshift_lhs": lhs, "lshift_rhs": rhs, } if lhs is not None:
				gates[output] = {
					"opcode": "__lshift__",
					"lhs": lhs,
					"rhs": rhs,
				}
			case {"output": output, "rshift_lhs": lhs, "rshift_rhs": rhs, } if lhs is not None:
				gates[output] = {
					"opcode": "__rshift__",
					"lhs": lhs,
					"rhs": rhs,
				}
			case {"output": output, "not": input, } if input is not None:
				gates[output] = {
					"opcode": "__invert__",
					"input": input,
				}
			case {"output": output, "eq": input, } if input is not None:
				gates[output] = {
					"opcode": "__eq__",
					"input": input,
				}
	
	p1 = resolve(b"a", gates, dict())
	
	gates[b"b"] = {
		"opcode": "__eq__",
		"input": str(p1).encode('utf-8'),
	}
	
	p2 = resolve(b"a", gates, dict())
	
	return p1, p2
