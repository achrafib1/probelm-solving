# https://codeforces.com/problemset/problem/1399/A


import sys

input = sys.stdin.readline


def solve():

    s = input().strip()
    n = int(s)
    arrs = list(map(int, input().split()))
    sorted_arr = sorted(arrs)
    ans = "YES"
    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i + 1] - sorted_arr[i] > 1:
            ans = "NO"
            break

    # --- OUTPUT ---
    print(ans)


line = input().strip()
if line:
    t = int(line)
    for _ in range(t):
        solve()




# 10min 2times
