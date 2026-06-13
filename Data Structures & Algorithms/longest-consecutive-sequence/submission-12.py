class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        for i in range(len(nums)):
            # if the number before nums[i] is in the set, it is not the start
            if nums[i]-1 in seen:
                continue
            else:
                # we know this is a sequence start
                length = 1
                current = nums[i]
                # check if next index is in the array, regardless of where
                while current+1 in seen:
                    length += 1
                    current +=1
                longest = max(longest, length)
        return longest