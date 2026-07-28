class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        bucket sort
        [2,3,6,2,4] -> max_stone = 6
        [0,0,2,1,1,0,1]
        """
        max_stone = max(stones)
        bucket = [0] * (max_stone + 1)
        first = second = max_stone
        while first > 0:
            # two max stone are the same weight, smashed them, and move to the next weight
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            
            # find the second largest stone
            actual_second = min(first - 1, second)
            while bucket[actual_second] != 0:  # skip the empty bucket
                actual_second -= 1
            
            # it's the last stone
            if actual_second == 0:
                return first

            # smashed them, and update the result
            smashed = first - actual_second
            second = actual_second
            first = max(smashed, second) 
            bucket[actual_second] -= 1
            bucket[first] -= 1
            bucket[smashed] += 1
            
        
        




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
