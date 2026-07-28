# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        bfs solution
        """
        queue = deque([(root, -101)])
        res = 0
        while queue:
            node, max_val = queue.popleft()
            if node:
                if node.val >= max_val:
                    res += 1
                    max_val = node.val
                queue.append((node.left, max_val))
                queue.append((node.right, max_val))
        return res



    def goodNodes_dfs(self, root: TreeNode) -> int:
        """
        improved
        """
        def dfs(root, max_val):
            if not root:
                return 0
            if root.val >= max_val:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, max_val) + dfs(root.right, max_val)
        
        return dfs(root, -101)

    def goodNodes_og(self, root: TreeNode) -> int:
        """
        root
        dfs traverse
        pass the current max val, have another count, if node.val >= max val, count += 1
            2
             4
            10 8
              4

        """
        self.count = 0
        def dfs(root, max_val):
            if not root:
                return
            
            if root.val >= max_val:
                self.count += 1
                dfs(root.left, root.val)
                dfs(root.right, root.val)
            else:
                dfs(root.left, max_val)
                dfs(root.right, max_val)
        dfs(root, -101)
        return self.count
            


        