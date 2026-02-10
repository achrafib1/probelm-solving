# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/


class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x = 0
        for i in range(len(operations)):
            if operations[i] == "X++" or operations[i] == "++X":
                x += 1
            else:
                x -= 1

        return x



#5min