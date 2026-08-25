# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cursor = root

        while cursor:
            # we want cursor to be between p and q's values or be equal to p or q's values
            if p.val < q.val:
                if p.val <= cursor.val <= q.val:
                    return cursor
                elif cursor.val > q.val:
                    cursor = cursor.left
                else:
                    cursor = cursor.right
            else:
                if q.val <= cursor.val <= p.val:
                    return cursor
                elif cursor.val > p.val:
                    cursor = cursor.left
                else:
                    cursor = cursor.right