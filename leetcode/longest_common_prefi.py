class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        if len(strs) == 1:
            ans = strs[0]
        if len(strs) > 1:
            min_str = min(strs)
            max_str = max(strs)
            for i in range(min(len(min_str), len(max_str))):
                if min_str[i] == max_str[i]:
                    ans += min_str[i]
                else:
                    break
        return ans


# second solution
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         ans=""
#         if (len(strs)==1):
#             ans=strs[0]
#         if(len(strs)>1):
#             min_str=min(strs)
#             max_str=max(strs)
#             for i in range(min(len(min_str),len(max_str))):
#                 if(min_str[i]==max_str[i]):
#                     ans+=min_str[i]
#                 else:
#                     break
#         return ans
