# https://www.hackerrank.com/challenges/insertionsort1/problem


#!/bin/python3

import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    key = arr[n - 1]
    i = n - 2
    while i >= 0 and key < arr[i]:
        arr[i + 1] = arr[i]
        i -= 1
        print(*arr)

    arr[i + 1] = key
    print(*arr)


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
