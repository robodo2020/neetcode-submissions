# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
            dfs solution
        """
        res = []
        
        def dfs(node, depth):
            if not node:
                return 
            if len(res) == depth:
                    res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return res

    def levelOrder_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        personally the most familiar solution
        """
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

        