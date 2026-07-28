# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # BFS
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            1
           2  3
          4 5 6 7

        queue = [1]
           1
          3  2
         6 7 4 5
        queue = [3,2]
        """
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
        