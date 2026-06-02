# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # involves depth of tree
        if not root:
            return 0
        return max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right), self.max_depth(root.left) + self.max_depth(root.right))

    def max_depth(self, root) -> int:
        if not root:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))