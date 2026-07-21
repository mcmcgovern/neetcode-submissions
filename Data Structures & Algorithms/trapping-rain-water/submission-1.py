class Solution:
    def trap(self, height: List[int]) -> int:
        # I am thinking outer two pointers loop
        # From left side, use extra pointer to keep advancing until a higher height is found
        # Then sum area between and move left pointer

        # Skip ground level squares until height is found for left pointer
        left = 0
        while left+1 < len(height) and height[left] < height[left+1]:
            left += 1

        # Advance right pointer to be its heighest
        right = len(height)-1
        while right-1 >= 0 and height[right] < height[right-1]:
            right -= 1

        # Now do core loop
        total_rain_area = 0
        while left < right:
            if height[left] <= height[right]:
                cursor = left + 1
                sandbars = 0
                while cursor < right and height[cursor] < height[left]:
                    sandbars += height[cursor]
                    cursor += 1
                total_rain_area += (cursor-left-1) * height[left] - sandbars
                left = cursor
            else:
                cursor = right - 1
                sandbars = 0
                while cursor > left and height[cursor] < height[right]:
                    sandbars += height[cursor]
                    cursor -= 1
                total_rain_area += (right-cursor-1) * height[right] - sandbars
                right = cursor
        return total_rain_area