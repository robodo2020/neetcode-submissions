class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Dijkstra algorithm, need review
        """
        graph = collections.defaultdict(list)

        for u, v, t in times:
            graph[u].append((v, t))
        
        min_heap = [(0, k)]
        t = 0
        visited = set()
        while min_heap:
            t1, v1 = heapq.heappop(min_heap)
            if v1 in visited:
                continue

            t = max(t, t1)
            visited.add(v1)            
            for v2, t2 in graph[v1]:
                heapq.heappush(min_heap, (t1 + t2, v2))
        return t if len(visited) == n else -1

        







            
                