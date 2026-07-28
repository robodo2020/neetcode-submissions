# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        use stack improved
        """
        stack = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            stack.append(node.val)
            dfs(node.right)
        dfs(root)
        return stack[k-1]


    def kthSmallest_stack(self, root: Optional[TreeNode], k: int) -> int:
        """
        use stack
        every time visit a node, add to stack, when done this node traverse, pop it
        the kth time popping the node is the k node
        """
        stack = []
        self.count = 0
        self.val = 0
        def dfs(root):
            if not root:
                return
            stack.append(root.val)
            dfs(root.left)
            res = stack.pop()
            self.count += 1
            if self.count == k:
                self.val = res
                return
            dfs(root.right)
        dfs(root)
        return self.val
            

    def kthSmallest_og(self, root: Optional[TreeNode], k: int) -> int:
        """
            10
          5    15
        3   8   
         4 7 9
         k = 5
        brute force
          get all the node, put in heap, pop out
        can utilize bst structure: ?
        """
        min_heap = []
        
        def dfs(root):
            if not root:
                return
            heapq.heappush(min_heap, root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        node = None
        for i in range(k):
            node = heapq.heappop(min_heap)
        return node


        