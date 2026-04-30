# https://leetcode.com/problems/decode-string/


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        if "[" not in s:
            return s

        k = 0
        new_s = ""
        count = 0
        n = ""
        i = 0
        ans = ""
        while i < len(s):
            if s[i].isdigit():
                n += s[i]
            elif s[i] == "[":

                k = int(n)
                n = ""
                count = 1
                j = i + 1
                while j < len(s):
                    if s[j] == "[":
                        count += 1
                    if s[j] == "]":
                        count -= 1

                    if count == 0:
                        break
                    j += 1

                new_s = s[i + 1 : j]

                curr_ans = self.decodeString(new_s)

                ans += k * curr_ans

                i = j
            else:
                ans += s[i]

            i += 1

        return ans
