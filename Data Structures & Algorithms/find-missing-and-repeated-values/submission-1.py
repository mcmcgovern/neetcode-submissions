class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        counts = {}
        for num_list in grid:
            for num in num_list:
                if num in counts:
                    counts[num] += 1
                    repeated = num
                else:
                    counts[num] = 1

        for i in range(1, (len(grid) ** 2) + 1):
            if i not in counts:
                missing = i
                break

        return [repeated, missing]