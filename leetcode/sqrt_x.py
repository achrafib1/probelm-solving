# https://leetcode.com/problems/sqrtx/description/


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # ans=1
        # if(x>1):
        #     while(ans*ans<=x):
        #         ans+=1
        #     ans-=1
        # else:
        #     ans=x

        # return ans

        ans = 1
        left = 1
        right = x // 2
        if x > 1:

            while left <= right:

                mid = (left + right) // 2

                if mid * mid == x:
                    ans = mid
                    break
                elif mid * mid > x:
                    right = mid - 1
                else:
                    ans = mid
                    left = mid + 1
        else:
            ans = x

        return ans
