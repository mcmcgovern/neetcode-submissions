# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we know root is not null, same for p and q
        # we are dealing with a BST
        # each node is unique
        smaller = min(p.val, q.val)
        larger = max(q.val, p.val)
        current_node = root
        while current_node:
            if smaller <= current_node.val <= larger:
                return current_node
            elif current_node.val > larger:
                current_node = current_node.left
            else:
                current_node = current_node.right