# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cursor = root
        smaller = p if p.val < q.val else q
        larger = p if smaller is q else q

        while cursor:
            # we want cursor to be between p and q's values or be equal to p or q's values
            if smaller.val <= cursor.val <= larger.val:
                return cursor
            elif cursor.val > larger.val:
                cursor = cursor.left
            else:
                cursor = cursor.right
            