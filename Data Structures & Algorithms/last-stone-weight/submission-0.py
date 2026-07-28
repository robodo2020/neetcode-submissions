class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        push to max heap
        take the fist 2 of them out, smash them, put it back
        until there's len 0 or 1
        """
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            a, b = heapq.heappop(max_heap), heapq.heappop(max_heap)
            smashed = abs(a - b)
            if smashed > 0:
                heapq.heappush(max_heap, -smashed)
        
        return -max_heap[0] if len(max_heap) == 1 else 0
