# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # optimal should use DFS to avoid dedoing work
        def height(root) -> int:
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        left = height(root.left)
        right = height(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)