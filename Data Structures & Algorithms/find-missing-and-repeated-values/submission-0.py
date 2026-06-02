class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid_nums = []
        for num_list in grid:
            for num in num_list:
                grid_nums.append(num)

        grid_nums = sorted(grid_nums)
        seen_set = set()
        # num_set = set([num for num in range(1, len(grid_nums) + 1)])
        for num in grid_nums:
            if num in seen_set:
                repeated = num
            else:
                seen_set.add(num)

        for i in range(1, len(grid_nums) + 1):
            if i not in seen_set:
                missing = i
        return [repeated, missing]