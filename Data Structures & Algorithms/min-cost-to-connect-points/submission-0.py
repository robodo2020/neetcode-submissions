class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points):
                if i == j:
                    continue
                m = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((j, m))
        
        min_heap = [(0, 0)] # weight, node
        w = 0
        visited = set()
        while len(visited) < len(points):
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            
            visited.add(n1)
            w += w1
            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w2, n2))
        return w
