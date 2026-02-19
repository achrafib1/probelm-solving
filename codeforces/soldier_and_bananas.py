# https://codeforces.com/problemset/problem/546/A


import sys

input = sys.stdin.readline


def solve():

    s = input().strip()
    k, n, w = map(int, s.split())
    # n = int(s)
    # arr = list(map(int, input().split()))

    ans = k * (w * (1 + w) // 2) - n if k * (w * (1 + w) // 2) >= n else 0

    # --- OUTPUT ---
    print(ans)


solve()
