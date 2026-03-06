# https://www.hackerrank.com/challenges/countingsort1/problem


#!/bin/python3

import math
import os
import random
import re
import sys


def countingSort(arr):
    ans = [0 for i in range(100)]

    for i in range(len(arr)):
        ans[arr[i]] += 1

    return ans


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()


#5min