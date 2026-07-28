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
        visited = {}
        def dfs(n):
            if n in visited:
                return visited[n]
            new_n = Node(n.val)
            visited[n] = new_n

            for nei in n.neighbors:
                new_n.neighbors.append(dfs(nei))
            return new_n
        return dfs(node) if node else None
                
            
        