# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # if p and not q or q and not p:
        #     return False

        # return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # stack solution
        stack = [(p, q)]
        while stack:
            p_node, q_node = stack.pop()
            if not p_node and not q_node:
                continue
            if p_node and not q_node or q_node and not p_node:
                return False
            if p_node.val == q_node.val:
                stack.append((p_node.left, q_node.left))
                stack.append((p_node.right, q_node.right))
            else:
                return False
        return True





