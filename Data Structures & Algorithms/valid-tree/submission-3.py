class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
         0
        1  2  3
       4

          0
         1
       2
      3
      does having cycle means not a tree?
      also, how many edges? any node alone?

      but, notice it's undirected graph problem
        """
        if len(edges) != n - 1:
            return False
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in graph[node]:
                if nei == parent: # skip checking the path that we just came from
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n