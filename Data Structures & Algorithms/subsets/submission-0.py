class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                all_subsets.append(subset.copy())
                return
            
            # with
            subset.append(nums[i])
            dfs(i + 1)
            # without
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return all_subsets