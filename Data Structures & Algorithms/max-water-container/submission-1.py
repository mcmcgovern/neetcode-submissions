class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # definitely no sorting, order matters
        # start at left and right, calculate height between * distance of indexes
        left, right = 0, len(heights)-1
        current_max = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            current_max = max(area, current_max)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return current_max