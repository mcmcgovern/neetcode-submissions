class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # squared = [num*num for num in nums]
        # return sorted(squared)

        # loop through nums to find closest positive number to zero
        # after finding this pivot, use two pointers, 
        # one advancing forwards and one backwards 
        # comparing each time with absolute values 
        squares = []

        # simple two pointers test
        left = 0
        right = len(nums)-1

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                squares.append(nums[right] ** 2)
                right -= 1
            elif abs(nums[left]) > abs(nums[right]):
                squares.append(nums[left] ** 2)
                left += 1
            else:
                squares.append(nums[left] ** 2)
                left += 1

        return squares[::-1]







        # find pivot closest to zero
        # for i in range(len(nums)):
        #     if nums[i] < 0:
        #         continue
        #     elif nums[i] == 0 or (i > 0 and nums[i-1] < 0):
        #         break

        # # use two pointers to go forwards / backwards
        # forwards_pointer = i
        # backwards_pointer = i-1
        # while len(nums) > len(squares):
        #     if forwards_pointer >= len(nums):
        #         squares.append(nums[backwards_pointer] ** 2)
        #         backwards_pointer -= 1
        #         continue
        #     elif backwards_pointer < 0:
        #         squares.append(nums[forwards_pointer] ** 2)
        #         forwards_pointer += 1
        #         continue

        #     if abs(nums[forwards_pointer]) > abs(nums[backwards_pointer]):
        #         squares.append(nums[backwards_pointer] ** 2)
        #         backwards_pointer -= 1
        #     elif abs(nums[forwards_pointer]) < abs(nums[backwards_pointer]):
        #         squares.append(nums[forwards_pointer] ** 2)
        #         forwards_pointer += 1
        #     else:
        #         squares.append(nums[backwards_pointer] ** 2)
        #         squares.append(nums[backwards_pointer] ** 2)
        #         forwards_pointer += 1
        #         backwards_pointer -= 1

        # return squares