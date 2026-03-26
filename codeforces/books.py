# https://codeforces.com/contest/279/problem/B


import sys

input = sys.stdin.readline


def solve():

    s = input().strip()
    n, t = map(int, s.split())
    arr = list(map(int, input().split()))

    left = 0
    ans = 0
    curr_sum = 0

    for right in range(len(arr)):
        curr_sum += arr[right]

        while curr_sum > t:
            curr_sum -= arr[left]
            left += 1

        ans = max(ans, right - left + 1)

    # --- OUTPUT ---
    print(ans)


solve()
