# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # use queue
        levels = []
        queue = deque()
        queue.append([root])
        while queue:
            current_level = queue.popleft()
            vals = []
            next_level = []
            for node in current_level:
                vals.append(node.val)
                node.left and next_level.append(node.left)
                node.right and next_level.append(node.right)
            levels.append(vals)
            if next_level:
                queue.append(next_level)
        return levels