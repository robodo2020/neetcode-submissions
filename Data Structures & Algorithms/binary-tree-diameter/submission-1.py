# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        DFS
          1
           2
          3 4
         5
        """
        self.res = 0
        
        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            self.res = max(self.res, left + right) # calculate the max diameter
            return 1 + max(left, right) # the max diameter of the current node
        dfs(root)
        return self.res

        