class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        stack = [] # will store tuples: (temp, index)
        output = [0] * len(temperatures)
        # index is important
        for i, temp in enumerate(temperatures): # [2, 3, 1, 4] => [1, 0, 1, 0]
            while stack and temp > stack[-1][0]:
                stack_top_temp, stack_top_index = stack.pop()
                output[stack_top_index] = i - stack_top_index
            stack.append((temp, i))
        return output