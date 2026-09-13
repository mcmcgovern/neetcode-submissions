# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        current_max = 0

        def dfs(node) -> int:
            if not node:
                return 0

            nonlocal current_max
            left = dfs(node.left)
            right = dfs(node.right)
            current_max = max(current_max, left + right)
            return 1 + max(left, right)

        dfs(root)
        return current_max