#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(x, y, z):
    total = x + y/100 * x + z/100 * x
    return int(total)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)