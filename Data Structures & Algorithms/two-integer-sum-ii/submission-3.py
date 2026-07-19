class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Try binary search
        for i in range(len(numbers)):
            seeking = target - numbers[i]

            left, right = 0, len(numbers)-1
            while left <= right:
                mid = (left+right)//2
                if numbers[mid] == seeking:
                    return [i+1, mid+1]
                elif numbers[mid] > seeking:
                    right = mid - 1
                else:
                    left = mid + 1
            