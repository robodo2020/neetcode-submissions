class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        for n in nums:
            heapq.heappush(max_heap, -n)
        
        res = None
        for i in range(k):
            res = heapq.heappop(max_heap)
        return -res