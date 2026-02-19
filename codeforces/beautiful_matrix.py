# https://codeforces.com/problemset/problem/263/A

import sys

input = sys.stdin.readline


def solve():

    mat = []
    for i in range(5):
        row = list(map(int, input().split()))
        mat.append(row)

    ans = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                ans = abs(i - 2) + abs(j - 2)
                break

    # --- OUTPUT ---
    print(ans)


solve()
