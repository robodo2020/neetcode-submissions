# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        optimized
        """
        self.result = False
        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot: # one of is has node, another doesn't
                return False
            if root.val != subRoot.val:
                return False
            return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
        
        def dfs(root, subRoot):
            if not root:
                return False
            return sameTree(root, subRoot) or dfs(root.left, subRoot) or dfs(root.right, subRoot)
        
        # since the problem ensure at least one node in each root, no need to considr base case oherwise:
        if not root:
            return False
        if not subRoot:
            return True
        
        return dfs(root, subRoot) 


    def isSubtree_og(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        my original solution
        1. traverse the root, using dfs
        2. until and root node val == subroot val, start checking
            traverse subroot to see if all node are the same
            
        """
        self.result = False
        def check_subroot(root, sub_root):
            if not root and not sub_root:
                return True
            if root and sub_root:
                if root.val != sub_root.val:
                    return False
                return check_subroot(root.left, sub_root.left) and check_subroot(root.right, sub_root.right)
            if root or sub_root:
                return False
        
        
        def dfs(root, sub_root):
            if not root:
                return None
        
            if root.val == subRoot.val:
                res = check_subroot(root, subRoot)
                if res:
                    self.result = True
            dfs(root.left, subRoot)
            dfs(root.right, subRoot)
        
        dfs(root, subRoot)
        return self.result
                
            


