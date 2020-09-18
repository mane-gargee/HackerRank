#!/bin/python3

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
    t1 = meal_cost
    t2 = tip_percent * t1/100
    t3 = tax_percent * t1/100
    print(round(t1+t2+t3))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
