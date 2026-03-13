# https://leetcode.com/problems/assign-cookies/description/?envType=daily-question&envId=2024-01-01


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        ans = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ans += 1
                i += 1

            j += 1

        return ans
