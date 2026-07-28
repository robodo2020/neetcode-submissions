# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
               8
           5       15
         2  6    12   17
        0 3 4 7 9 13 16 18
        False: 4 doesn't meet the requirement

        keep the left / right bound
        5, 0-8
        2, 0-5
        0, 0-5 v
        3, 2-5 v
        6, 5-8 v
        4, 5-6 x
        dfs
            5
           4  6
             3 7
        """
        self.result = True
        
        def dfs(root, left, right):
            if not root:
                return
            if not left < root.val < right:
                self.result = False
            
            dfs(root.left, left, root.val)
            dfs(root.right, root.val, right)
        dfs(root, -1001, 1001)
        return self.result
                



        