# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        each node, check the height of each node,
        and to do the compare, check the height of left & right node, and to see if it's balanced
        
        """
        self.result = True
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1:
                self.result = False
            return 1 + max(left, right)
        dfs(root)
        return self.result