class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # o(n**2) attempt
        longest = 0
        for i, h in enumerate(heights):
            # take each height and extend it left and right (as long as >= h)
            left = i
            while left >= 0 and heights[left] >= h:
                left -= 1
            if left < 0 or heights[left] < h:
                left += 1
            right = i
            while right < len(heights) and heights[right] >= h:
                right += 1
            if right >= len(heights) or heights[right] < h:
                right -= 1
            print(i, h, heights[left], heights[right], left, right)
            longest = max(longest, h, (h*(right-left+1)))
        return longest













        # # Attempt 1
        # # Iterate through heights, push current one to stack
        # # If current >= top of stack, it can be a part of a multi-bar rectangle
        # longest = 0
        # stack = [] # push current and min to stack
        # for h in heights:
        #     # If we encounter a very large bar, it could potentially become the max
        #     longest = max(h, longest)
            
        #     # when to pop?? Need stack values to be increasing for rect to be formed
        #     # Consider that each h could be the start of largest rect
        #     if stack and h < stack[-1][0]:
        #         stack.pop()
            
        #     # Always push node and current min to stack
        #     stack.append((h, min(h, stack[-1][1])))
        # return longest