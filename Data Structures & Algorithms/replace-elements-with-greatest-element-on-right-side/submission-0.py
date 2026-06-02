class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # current_max = float('-inf')

        # for i in range(len(arr) - 1, -1, -1):

        #     # if arr[i] < current_max:
        #     current_max = max(current_max, arr[i])
        #     arr[i-1] = current_max
        # arr[-1] = -1
        # return arr

        right_maxes = [float('-inf')] * len(arr)
        current_max = float('-inf')
        for i in range(len(arr)-2, -1, -1):
            current_max = max(current_max, arr[i+1])
            right_maxes[i] = current_max

        for i in range(len(arr)-1, -1, -1):
            arr[i] = right_maxes[i]

        arr[-1] = -1

        return arr