# https://codeforces.com/problemset/problem/1742/A


import sys

input = sys.stdin.readline


def solve():

    s = input().strip()
    a, b, c = map(int, s.split())
    ans = "NO"
    if a + b == c:
        ans = "YES"
    if a + c == b:
        ans = "YES"
    if b + c == a:
        ans = "YES"

    # --- OUTPUT ---
    print(ans)


line = input().strip()
if line:
    t = int(line)
    for _ in range(t):
        solve()
