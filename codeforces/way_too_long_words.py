# https://codeforces.com/problemset/problem/71/A


import sys

input = sys.stdin.readline


def solve():

    s = input().strip()
    ans = s[0] + str(len(s) - 2) + s[len(s) - 1] if len(s) > 10 else s

    # --- OUTPUT ---
    print(ans)


line = input().strip()
if line:
    t = int(line)
    for _ in range(t):
        solve()
