class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Set default of 0 since decreasing list will never have a warmer temp
        result = [0] * len(temperatures)
        # Create stack to push current temp candidate until warmer temp is found
        stack = []
        for index, temp in enumerate(temperatures):
            # Before pushing to stack, we need to know if the current temp 
            # is greater than the stack top and if so record it
            while stack and stack[-1][0] < temp:
                top_temp, top_index = stack.pop()
                result[top_index] = index - top_index
            # Always push the current temp, index candidate to stack
            stack.append((temp, index))
        return result