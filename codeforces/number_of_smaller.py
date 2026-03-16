# https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B


import sys

input = sys.stdin.readline


def solve():

    s = input().strip()
    n, m = map(int, s.split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    i = 0
    j = 0
    ans = []
    while i < len(arr1) and j < len(arr2):
        if arr2[j] <= arr1[i]:
            ans.append(i)
            j += 1
        else:
            i += 1

    while j < len(arr2):
        ans.append(i)
        j += 1
    # --- OUTPUT ---
    print(*ans)


solve()
