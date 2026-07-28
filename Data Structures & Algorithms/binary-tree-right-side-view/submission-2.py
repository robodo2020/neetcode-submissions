# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
            dfs solution
        """
        res = []

        def dfs(root, depth):
            if not root:
                return
            
            if depth == len(res):
                res.append(0) # mark as the bucket
            
            res[depth] = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return res
            
            
    
    def rightSideView_improved(self, root: Optional[TreeNode]) -> List[int]:
        """
        each level, the right most node
        bfs
        """
        res = []
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
                res.append(cur_level[-1])
        return res

    def rightSideView_bfs_og(self, root: Optional[TreeNode]) -> List[int]:
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