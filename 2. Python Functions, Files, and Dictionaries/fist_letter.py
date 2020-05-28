#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    newlst = []
    for word in s:
        word = word.capitalize()
        newlst.append(word)
        print(newlst)
    return " ".join(newlst)


print(solve(input("Enter name: ")))