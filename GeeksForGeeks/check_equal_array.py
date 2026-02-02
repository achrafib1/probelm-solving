# https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1


class Solution:
    def checkEqual(self, a, b) -> bool:
        ans = True
        sorted_a = sorted(a)
        sorted_b = sorted(b)
        for i in range(len(a)):
            if sorted_a[i] != sorted_b[i]:
                ans = False
                break

        return ans


# 3min
