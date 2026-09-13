class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # iterate backwards through array to find greatest element to right
        current_max = arr[-1]
        right_maxes = [current_max] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            current_max = max(current_max, arr[i])
            right_maxes[i] = current_max
        right_maxes = right_maxes[1:]
        right_maxes.append(-1)
        return right_maxes