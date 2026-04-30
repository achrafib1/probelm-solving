# https://leetcode.com/problems/my-calendar-i/


class MyCalendar(object):
    def __init__(self):
        self.events = []

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """

        ans = True

        left = 0
        right = len(self.events) - 1

        idx = len(self.events)

        while left <= right:
            mid = int((left + right)) // 2

            if self.events[mid][0] >= startTime:
                idx = mid
                right = mid - 1
            else:
                left = mid + 1

        if idx < len(self.events) and endTime > self.events[idx][0]:
            ans = False

        elif idx > 0 and self.events[idx - 1][1] > startTime:
            ans = False

        else:
            self.events.insert(idx, [startTime, endTime])

        return ans


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
