# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # NOT BST, just binary tree
        # We can keep track of a current max as we go down
        # Try DFS

        # Tree is non-empty
        # Root should always be a good node automatically

        def dfs(node: TreeNode, current_max: int) -> int:
            if not node:
                return 0

            updated_max = max(node.val, current_max)
            good_count = 0
            good_count += 1 if node.val >= current_max else 0
            good_count += dfs(node.left, updated_max)
            good_count += dfs(node.right, updated_max)
            return good_count

        return dfs(root, -101)



