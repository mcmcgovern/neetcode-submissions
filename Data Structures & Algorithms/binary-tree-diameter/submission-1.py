# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # not necessarily starting from, or passing through root
        # definitely want to do DFS
        if not root:
            return 0

        # we want the max, either starting at the root (current node) or not
        diameter = self.depth(root.left) + self.depth(root.right)
        return max(diameter, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))