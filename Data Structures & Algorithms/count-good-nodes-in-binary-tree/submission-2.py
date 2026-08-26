# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # try BFS
        queue = deque()
        queue.append((root, root.val)) # node, max
        good_count = 0
        while queue:
            queue_length = len(queue)
            for _ in range(queue_length):
                node, prev_max = queue.popleft()
                if node.val >= prev_max:
                    good_count += 1
                node.left and queue.append((node.left, max(node.val, prev_max)))
                node.right and queue.append((node.right, max(node.val, prev_max)))
        return good_count
