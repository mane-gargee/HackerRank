#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    if N%2==0:
        if 2<N<=5:
            print("Not Weird")
        elif 6<N<=20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")
