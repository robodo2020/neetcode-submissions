# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            1
           2  3
          4 5 6 7

          1
         3  2
        7 6 4 5

        """
        # base case, if root is None, don't need to do anything
        if root is None:
            return None
        # if root has something, invert it
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        