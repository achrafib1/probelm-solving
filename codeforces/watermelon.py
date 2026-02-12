# https://codeforces.com/problemset/problem/4/A


import sys

input = sys.stdin.readline


def solve():

    s = int(input().strip())

    # --- OUTPUT ---
    print("YES" if s % 2 == 0 and s > 2 else "NO")


solve()
