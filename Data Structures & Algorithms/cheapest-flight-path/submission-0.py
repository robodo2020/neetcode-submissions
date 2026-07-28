class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
                0
            1        
                   2
            3

            dfs

            k: max stops
        """
        graph = collections.defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        
        result = float('inf')
        visited = set()
        def dfs(i, cost, n_stops):
            nonlocal result
            if n_stops - 1 > k:
                return
            if i == dst:
                result = min(result, cost)
                return
            
            visited.add(i)
            for nxt, nxt_cost in graph[i]:
                if nxt not in visited:
                    dfs(nxt, cost + nxt_cost, n_stops + 1)
            visited.remove(i)
            return
        
        dfs(src, 0, 0)
        return result if result != float('inf') else -1

                

                
