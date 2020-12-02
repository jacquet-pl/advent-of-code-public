#!/bin/false
# SPDX-License-Identifier: AGPL-3.0-or-later
# Copyright 2021, jacquet-pl <92673275+jacquet-pl@users.noreply.github.com>

from .All_in_a_Single_Night import main as All_in_a_Single_Night
from .Doesn_t_He_Have_Intern_Elves_For_This import main as Doesn_t_He_Have_Intern_Elves_For_This
from .I_Was_Told_There_Would_Be_No_Math import main as I_Was_Told_There_Would_Be_No_Math
from .Matchsticks import main as Matchsticks
from .Not_Quite_Lisp import main as Not_Quite_Lisp
from .Password_Philosophy import main as Password_Philosophy
from .Perfectly_Spherical_Houses_in_a_Vacuum import main as Perfectly_Spherical_Houses_in_a_Vacuum
from .Probably_a_Fire_Hazard import main as Probably_a_Fire_Hazard
from .Report_Repair import main as Report_Repair
from .Some_Assembly_Required import main as Some_Assembly_Required
from .The_Ideal_Stocking_Stuffer import main as The_Ideal_Stocking_Stuffer

solver_by_year_by_day = {
	'2015': {
		'1': Not_Quite_Lisp,
		'2': I_Was_Told_There_Would_Be_No_Math,
		'3': Perfectly_Spherical_Houses_in_a_Vacuum,
		'4': The_Ideal_Stocking_Stuffer,
		'5': Doesn_t_He_Have_Intern_Elves_For_This,
		'6': Probably_a_Fire_Hazard,
		'7': Some_Assembly_Required,
		'8': Matchsticks,
		'9': All_in_a_Single_Night,
	},
	'2020': {
		'1': Report_Repair,
		'2': Password_Philosophy,
	},
}
