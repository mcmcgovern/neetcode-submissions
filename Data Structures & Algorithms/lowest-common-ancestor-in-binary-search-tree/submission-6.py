# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cursor = root
        smaller = min(p.val, q.val)
        larger = max(p.val, q.val)

        while cursor:
            # we want cursor to be between p and q's values or be equal to p or q's values
            if smaller <= cursor.val <= larger:
                return cursor
            elif cursor.val > larger:
                cursor = cursor.left
            else:
                cursor = cursor.right
            