# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # simple, brute force is to count all nodes, build array of all nodes in sorted order
        nodes = []
        def dfs(root) -> None:
            if root == None:
                return

            nonlocal nodes
            if root.left:
                dfs(root.left)
            nodes.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)

        # now that nodes has all vals in sorted order, step through k
        return nodes[k-1]