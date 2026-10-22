class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Attempt to use bucket sort
        # Step 1: count how many of each occur
        counts = [0] * 3 # only three options: (0,1,2)
        for num in nums:
            counts[num] += 1

        # Step 2: iterate over each count to reconstruct array
        i = 0
        for index, count in enumerate(counts):
            for j in range(count):
                nums[i] = index
                i += 1