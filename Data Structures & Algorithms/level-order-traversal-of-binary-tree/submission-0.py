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
        levels = []
        queue = [root]
        while queue:
            current_level = queue.copy()
            level = []
            for i in range(len(current_level)):
                current_node = queue.pop()
                level.append(current_node.val)
                print(current_node.val)
                if current_node.left:
                    queue.insert(0, current_node.left)
                if current_node.right:
                    queue.insert(0, current_node.right)
            levels.append(level)
        return levels