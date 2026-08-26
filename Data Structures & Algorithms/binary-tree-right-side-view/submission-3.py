# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        queue.append(root)
        right_side_vals = []

        while queue:
            queue_length = len(queue)
            for i in range(queue_length):
                node = queue.popleft()
                if node:
                    node.left and queue.append(node.left)
                    node.right and queue.append(node.right)
                    if i == queue_length-1:
                        right_side_vals.append(node.val)
        return right_side_vals