class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Dijkstra algorithm, need review
        """
        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        min_heap = [(0, k)] # time, k - for time to take min_heap action
        visited = set()
        t = 0
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited: # already processed, and the previous one has less time, so no need to process this again
                continue
            visited.add(n1)
            t = max(t, w1) # update how much time needed now

            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))
        return t if len(visited) == n else -1

        







            
                