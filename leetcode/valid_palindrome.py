# https://leetcode.com/problems/valid-palindrome/description/


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = 0
        ans = True
        clear_s = "".join([char for char in s if char.isalnum()]).lower()
        right = len(clear_s) - 1
        while left <= right:
            if clear_s[left] != clear_s[right]:
                ans = False
                break

            left += 1
            right -= 1

        return ans
