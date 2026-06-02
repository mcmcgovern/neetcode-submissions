class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers, left right
        # find tallest on both sides, checking area at each step
        # discard outer bounary areas since they could not hold water
        largest_area = 0
        left, right = 0, len(heights)-1

        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            largest_area = max(largest_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return largest_area