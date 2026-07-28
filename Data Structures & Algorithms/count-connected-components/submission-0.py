class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        mapping = collections.defaultdict(list)
        for u, v in edges:
            mapping[u].append(v)
            mapping[v].append(u)
        
        visited = set()
        def dfs(cur, pre):
            if cur in visited:
                return
            visited.add(cur)
            for nxt in mapping[cur]:
                if nxt == pre:
                    continue
                dfs(nxt, cur)
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        return count
