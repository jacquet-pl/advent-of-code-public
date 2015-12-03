#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

from .I_Was_Told_There_Would_Be_No_Math import main as I_Was_Told_There_Would_Be_No_Math
from .Not_Quite_Lisp import main as Not_Quite_Lisp
from .Perfectly_Spherical_Houses_in_a_Vacuum import main as Perfectly_Spherical_Houses_in_a_Vacuum

solver_by_year_by_day = {
	'2015': {
		'1': Not_Quite_Lisp,
		'2': I_Was_Told_There_Would_Be_No_Math,
		'3': Perfectly_Spherical_Houses_in_a_Vacuum,
	},
}
