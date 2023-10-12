#! /usr/bin/env python3

"""unittesting cosmicpathoptimitzation.py solution
"""

__author__ = "Lluis Fabregat Riesco"
__date__ = "Oct. 10, 2023"

import unittest
from cosmicpathoptimization import answer


class TestCosmic(unittest.TestCase):
    """ Test from cosmicpathoptimitzation.py solution
    """

    def test1_answer(self) -> None:
        """Test cosmicpathoptimitzation.py answer function"""
        num = 6
        data = [313, 310, 328, 321, 302, 315]
        self.assertEqual(
            answer(data, num), 314, 'Broken')

    def test2_answer(self) -> None:
        """Test cosmicpathoptimitzation.py answer function"""
        num = 4
        data = [273, 261, 268, 275]
        self.assertEqual(
            answer(data, num), 269, 'Broken')

    def test3_answer(self) -> None:
        """ Test cosmicpathoptimitzation.py answer function"""
        num = 7
        data = [2389, 2401, 2385, 2381, 2409, 2377, 2383]
        self.assertEqual(
            answer(data, num), 2389, 'Broken')

    def test4_answer(self) -> None:
        """ Test cosmicpathoptimitzation.py answer function"""
        num = 1
        data = [0]
        self.assertEqual(
            answer(data, num), 0, 'Broken')

    def test5_answer(self) -> None:
        """ Test cosmicpathoptimitzation.py answer function"""
        num = 4
        data = [100000, 99999, 0, 1]
        self.assertEqual(
            answer(data, num), 50000, 'Broken')

    def test6_answer(self) -> None:
        """ Test cosmicpathoptimitzation.py answer function"""
        num = 15
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(
            answer(data, num), 8, 'Broken')


if __name__ == "__main__":
    unittest.main(verbosity=2)
