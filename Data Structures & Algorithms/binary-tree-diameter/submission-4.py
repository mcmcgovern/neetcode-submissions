# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def max_depth(node) -> int:
            if not node:
                return 0

            left = max_depth(node.left)
            right = max_depth(node.right)
            return 1 + max(left, right)

        left = max_depth(root.left)
        right = max_depth(root.right)
        return max(left + right, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))