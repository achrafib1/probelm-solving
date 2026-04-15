# https://leetcode.com/problems/time-needed-to-buy-tickets/description/


from collections import deque


class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        queue = deque()
        target = k
        for i in range(len(tickets)):
            queue.append(tickets[i])

        ans = 0
        while queue:
            if target == -1:
                break

            if queue[0] - 1 > 0:
                queue.append(queue[0] - 1)

            if target == 0:
                if queue[target] - 1 > 0:
                    target = len(queue) - 2
                else:
                    target = -1
            else:
                target -= 1

            queue.popleft()
            ans += 1

        return ans
