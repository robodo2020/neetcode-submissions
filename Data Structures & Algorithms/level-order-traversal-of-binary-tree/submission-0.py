# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
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
                result.append(cur_level)
        return result

        