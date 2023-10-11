#! /usr/bin/env python3
"""
Kattis "Cosmis path optimization" problem

Calculates the average temperature of a planet given some readings in Kelvin

Algorithm:
    1. Read the first line as number of temperatures
    2. Read the second line as space separated temperatures
    3. Split the second line into list of temperatures
    4. Iterate through the list and adds the value of all the readings
    5. Divides the total value into the number of temperatures
    6. Prints the average temperature rounded
"""
__author__ = "Lluis Fabregat Riesco"
__date__ = "Oct. 10, 2023"

import sys
from typing import List


def answer(data: List[int], n: int) -> int:
    """ Calculates the average temperature given the readings

    Args:
        data (List[int]): list of integers as temperature
        n (int): number of readings

    Returns:
        average (int): average value of all temperatures
    """
    average = 0
    add = 0
    for temp in data:
        add += temp
    average = int(add / n)
    return average


def solve() -> None:
    """ Reads the input and uses answer function
    """
    num = int(input())
    temps = [int(temp) for temp in sys.stdin.readline().strip().split()]
    print(answer(temps, num))


if __name__ == "__main__":
    solve()
