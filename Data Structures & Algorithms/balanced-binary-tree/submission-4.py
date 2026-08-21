# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root: Optional[TreeNode]) -> tuple:
            if not root:
                return (True, 0)

            left_is_balanced, left_height = dfs(root.left)
            right_is_balanced, right_height = dfs(root.right)
            balanced = left_is_balanced and right_is_balanced and (
                abs(left_height - right_height) <= 1
            )
            return (balanced, 1 + max(left_height, right_height))
        return dfs(root)[0]