# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
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
            


        