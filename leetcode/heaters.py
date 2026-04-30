# https://leetcode.com/problems/heaters/


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """

        houses.sort()
        heaters.sort()

        def checkheaterradius(n, houses, heaters):

            curr_house = 0
            for i in range(len(heaters)):

                while curr_house < len(houses):
                    if (
                        houses[curr_house] < heaters[i] - n
                        or houses[curr_house] > heaters[i] + n
                    ):
                        break
                    else:
                        curr_house += 1

                if curr_house >= len(houses):
                    return True

            if curr_house < len(houses):
                return False
            else:
                return True

        left = 0
        right = max(max(houses), max(heaters)) - min(min(houses), min(heaters))
        ans = right

        while left <= right:
            mid = int((left + right)) // 2

            if checkheaterradius(mid, houses, heaters):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1

        return ans
