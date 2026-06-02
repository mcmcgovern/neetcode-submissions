class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for num_list in grid:
            for num in num_list:
                counts[num] += 1

        for i in range(1, (len(grid) ** 2) + 1):
            if counts[i] == 0:
                missing = i
            elif counts[i] == 2:
                repeated = i

        return [repeated, missing]