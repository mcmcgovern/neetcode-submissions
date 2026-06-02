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
        
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.max_depth(root.left) - self.max_depth(root.right)) <= 1

    def max_depth(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))