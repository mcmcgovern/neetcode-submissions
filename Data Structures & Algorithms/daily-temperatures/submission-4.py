class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            # push (temp, index) to stack
            while stack and temp > stack[-1][0]:
                stack_top_temp, stack_top_index = stack.pop()
                result[stack_top_index] = index - stack_top_index
            stack.append((temp, index))
        return result