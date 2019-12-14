######################################################################
# Author: Samantha Schweinsberg
# Username: schweinsbergs
#
# Assignment: T06: Funky Functions Test Suite
# Purpose:  Test suite to test the function Thy wrote in Check 5 character functions
#
######################################################################
from Check_5_characters_functions import *
import sys

def testit(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """
    linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def character_test_suite():
    """
    This tests whether or not our function passes or fails a unit test.
    :return: None
    """
    testit(check_5_characters_functions("Willow") == True)
    testit(check_5_characters_functions("Axe") == False)
    testit(check_5_characters_functions("1234") == False)
    testit(check_5_characters_functions("12345") == True)
    testit(check_5_characters_functions("a") == False)
    testit(check_5_characters_functions("*#&@*#@") == True)
    testit(check_5_characters_functions("-34932093045") == True)
    testit(check_5_characters_functions("list[1,3,4]") == True)
    testit(check_5_characters_functions(2.6) == False)
character_test_suite()
