"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        node -> nei
        1
        [2]

        2 -> val
        nei -> 1, 3
        traverse the node hasn't visited
        """
        old_to_new = {} # if we visited the old node, meaning we already create a new copy for it, then redirect to the new copy
        def dfs(n):
            if n in old_to_new:
                return old_to_new[n]
            copy = Node(n.val)
            old_to_new[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None
                
            
        