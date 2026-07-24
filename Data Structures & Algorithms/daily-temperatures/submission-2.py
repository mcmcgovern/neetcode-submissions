class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        stack = [] # will store tuples: (temp, index)
        output = [0] * len(temperatures)
        # index is important
        for i, temp in enumerate(temperatures): # [2, 3, 1, 4] => [1, 0, 1, 0]
            while stack and temp > stack[-1][0]:
                stack_top = stack.pop()
                output[stack_top[1]] = i - stack_top[1]
            stack.append((temp, i))
        return output