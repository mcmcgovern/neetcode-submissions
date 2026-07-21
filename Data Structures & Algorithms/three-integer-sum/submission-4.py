class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First sort nums
        nums.sort()
        triplets = []
        seen = set()

        # [-2,0,1,1,2]
        # Using three pointers, start at leftmost and consider remaining array as window
        # Use same approach as two sum 2: check to see if sum > 0 and if so adjust right, else left
        for i in range(len(nums) - 2):
            num1 = nums[i]
            # remaining window is nums[i:]
            left, right = i+1, len(nums)-1
            while left < right:
                num2, num3 = nums[left], nums[right]
                if num1 + num2 + num3 == 0:
                    if (num1,num2,num3) not in seen:
                        triplets.append([num1,num2,num3])
                        seen.add((num1,num2,num3))
                    left += 1
                elif num1 + num2 + num3 > 0:
                    right -= 1
                else:
                    left += 1
        return triplets