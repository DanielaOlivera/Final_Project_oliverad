######################################################################
# Author: Daniela Olivera
# Username: oliverad
#
# Assignment: Final Project
# Purpose:  Test suite to test the angle_calculator function in Flower_Class.py
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################
import sys

from Flower_Class import *


def testit(did_pass):
    """
    Print the result of a unit test.

    :param did_pass: Boolean representing if the unit test passed or failed
    :return: None
    """
    # This function works correctly--it is verbatim from the text, Chapter 6
    linenum = sys._getframe(1).f_lineno                 # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def flower_class_test_suite():
    """
    The test_suite function utilizes the testit() function,
    and is designed to test the willaby_wallaby() function.

    :return: None
    """
    print("\nRunning the flower_class_test_suite().")
    ##########################################
    dani = Flower(pos=(0,0), num=3)
    testit(dani.angle_calculator() == 120)   # 360/3 is 120
    ella = Flower(pos=(0, 0), num=360)
    testit(ella.angle_calculator() == 1)




    ##########################################
    print("\nEnding the flower_class_testsuite().")


def main():
    """ A function that calculates the angle to turn based on number of sides

    :return: None
    """

    flower_class_test_suite()

if __name__ == "__main__":
    main()
