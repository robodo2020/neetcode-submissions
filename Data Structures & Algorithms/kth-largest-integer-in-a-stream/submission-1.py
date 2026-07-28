class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        heap: only root order is ensure == min_heap[0]
        have a len == k heap, so guarantee the first number is the kth largest
        """
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

        
