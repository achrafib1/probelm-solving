# https://leetcode.com/problems/valid-palindrome-ii/


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        ans = True
        while left < right:
            if s[left] != s[right]:
                ans1 = False
                ans2 = False
                if s[right - 1] == s[left]:
                    next_right = right - 1
                    next_left = left
                    ans1 = True
                    while next_left < next_right:
                        if s[next_left] != s[next_right]:
                            ans1 = False
                            break

                        next_left += 1
                        next_right -= 1

                    if ans1 == True:
                        break

                if s[left + 1] == s[right]:
                    next_right = right
                    next_left = left + 1
                    ans2 = True
                    while next_left < next_right:
                        if s[next_left] != s[next_right]:
                            ans2 = False
                            break

                        next_left += 1
                        next_right -= 1

                    if ans2 == True:
                        break

                if ans1 == False and ans2 == False:
                    ans = False
                    break

            left += 1
            right -= 1

        return ans
