# https://practice.geeksforgeeks.org/problems/array-subset-of-another-array2317/1


class Solution:
    # Function to check if a is a subset of b.
    def isSubset(self, a, b):
        ans = True
        freq_dict = {}
        for i in range(len(a)):
            freq_dict[a[i]] = freq_dict.get(a[i], 0) + 1
        for i in range(len(b)):
            if freq_dict.get(b[i], 0) == 0:
                ans = False
                break
            else:
                freq_dict[b[i]] -= 1

        return ans


# 13 min 2times
