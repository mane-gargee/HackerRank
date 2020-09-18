#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = bin(int(input().strip()))
    n = n[2:]
print(len(max(n.split('0'))))
