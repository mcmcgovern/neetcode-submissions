class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combos = []

        def dfs(i, current_combo, current_sum) -> None:
            if current_sum == target:
                combos.append(current_combo.copy())
                return
            if i >= len(nums) or current_sum > target:
                return

            # choose to include current
            current_combo.append(nums[i])
            dfs(i, current_combo, current_sum + nums[i])

            # choose not to include current
            current_combo.pop()
            dfs(i + 1, current_combo, current_sum)
        
        dfs(0, [], 0)
        return combos