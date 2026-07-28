# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        pre: first == root
            [1,2,3,4]
        in: first == leftmost
            [2,1,3,4]
        
        use pre to get the root by pre[0]
        then, find the index from inorder, and the left elements of that index, is the left side of the tree, otherwise the right side
        """
        if not preorder and not inorder:
            return None
        
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        return root