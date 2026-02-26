# https://www.geeksforgeeks.org/problems/selection-sort/1


class Solution:
    def selectionSort(self, arr):
        for i in range(len(arr)):
            min_v_i = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_v_i]:
                    min_v_i = j

            arr[min_v_i], arr[i] = arr[i], arr[min_v_i]

        return arr
