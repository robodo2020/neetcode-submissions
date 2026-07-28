# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        each level, the right most node
        bfs
        """
        level_nodes = []
        queue = collections.deque([root])
        while queue:
            l = len(queue)
            cur_level = []
            for _ in range(l):
                node = queue.popleft()
                if node:
                    cur_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if cur_level:
                level_nodes.append(cur_level)
        res = []
        for level in level_nodes:
            res.append(level[-1])
        return res