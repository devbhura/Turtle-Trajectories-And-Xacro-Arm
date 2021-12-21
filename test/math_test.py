#!/usr/bin/env python

"""
Unit test for math.py
"""
import unittest
from homework2.math import math_calc 
import numpy 
import rospy

class MyTestCase(unittest.TestCase):
    """
    Class for unit test
    """
    
    def test_something(self):
        """
        Test case for when t=0 
        """
        self.assertEquals(math_calc(1,1,1,0), (7, 0, 1, 0, 3, 0, 0, 6, 0))


if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, 'test_class_name', MyTestCase)