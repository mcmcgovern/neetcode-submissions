# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # store level nodes and current max
        count = 0
        queue = collections.deque([(root, float('-inf'))])
        while queue:
            q_length = len(queue)
            for i in range(q_length):
                current_node, current_max = queue.popleft()
                # print(current_node.val, current_max)
                # current node is good
                if current_node.val >= current_max:
                    count += 1
                    current_max = current_node.val

                if current_node.left:
                    queue.append((current_node.left, current_max))
                if current_node.right:
                    queue.append((current_node.right, current_max))

        return count