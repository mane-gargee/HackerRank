#!/bin/python3

import math
import os
import random
import re
import sys

def sumFun(matrix,row,col):
    sum1=0
    sum1 += matrix[row-1][col-1]
    sum1 += matrix[row-1][col]
    sum1 += matrix[row-1][col+1]
    sum1 += matrix[row][col]
    sum1 += matrix[row+1][col-1]
    sum1 += matrix[row+1][col]
    sum1 += matrix[row+1][col+1]
    return sum1

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max0=-63
    for i in range(1,5):
        for j in range(1,5):
            sum0 = sumFun(arr,i,j)
            if sum0>max0:
                max0 = sum0
    print(max0)
