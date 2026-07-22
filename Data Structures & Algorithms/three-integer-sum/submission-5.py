class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first sort the array
        nums.sort()
        triplets = []
        seen = set()

        for i in range(len(nums)-2):
            num1 = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                num2 = nums[left]
                num3 = nums[right]

                current_sum = num1+num2+num3
                if current_sum == 0:
                    # add to triplets
                    if (num1,num2,num3) not in seen:
                        triplets.append([num1,num2,num3])
                        seen.add((num1,num2,num3))
                    left += 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return triplets