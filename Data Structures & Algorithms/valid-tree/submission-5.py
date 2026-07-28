class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        map = collections.defaultdict(list)

        for u, v in edges:
            map[u].append(v)
            map[v].append(u)
        
        visited = set()
        def dfs(cur, pre):
            if cur in visited:
                return False
            
            visited.add(cur)
            for nxt in map[cur]:
                if nxt == pre:
                    continue
                if not dfs(nxt, cur):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n





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
                if nei == parend: # skip checking the path that we just came from
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n

