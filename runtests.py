#!/usr/bin/python2.2
# Python-based gopher server
# Module: main test runner
# COPYRIGHT #
# Copyright (C) 2002 John Goerzen
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# END OF COPYRIGHT #

import sys
# sys.path.insert("-1", "..")

import unittest
from pygopherd import *

def suite():
    tests = [initializationTest,
             GopherExceptionsTest,
             fileextTest,
             gopherentryTest,
             loggerTest
        ]
    suite = unittest.TestSuite()
    for module in tests:
        suite.addTest(unittest.findTestCases(module))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')

