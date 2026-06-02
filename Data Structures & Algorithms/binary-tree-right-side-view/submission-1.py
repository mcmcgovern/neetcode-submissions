# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level order traversal. represent rightmost node in levels where there is more than one node, else left
        if not root:
            return []

        queue = collections.deque()
        queue.append(root)
        view = []
        while queue:
            q_length = len(queue)
            # level_nodes = []
            for i in range(q_length):
                current_node = queue.popleft()
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                # level_nodes.append(current_node)
                if i == q_length-1:
                    view.append(current_node.val)
            # view.append(level_nodes[-1].val)
        return view