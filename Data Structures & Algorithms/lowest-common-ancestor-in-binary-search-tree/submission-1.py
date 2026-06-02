# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if self.is_ancestor(root.left, p) and self.is_ancestor(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)

        if self.is_ancestor(root.right, p) and self.is_ancestor(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)

        if self.is_ancestor(root, p) and self.is_ancestor(root, q):
            return root
        
    def is_ancestor(self, root, node) -> bool:
        if not root:
            return False

        if root.val == node.val:
            return True

        return self.is_ancestor(root.left, node) or self.is_ancestor(root.right, node)