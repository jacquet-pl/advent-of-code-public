#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

import pathlib
inputs_root = pathlib.Path(__file__).parent / 'inputs'

from solvers import solver_by_year_by_day

for year, solver_by_day in solver_by_year_by_day.items():
	for day, solver in solver_by_day.items():
		content = b''
		
		with open(inputs_root / year / day, mode='rb') as file:
			while chunk := file.read():
				content += chunk
		
		p1, p2 = solver(content)
		
		print(F'''{year=} {day=} {p1=} {p2=}''')
