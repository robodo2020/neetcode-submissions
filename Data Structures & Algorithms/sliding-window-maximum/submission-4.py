class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        [1,2,1,0,4,2,6]
         |
             |
        invariant:
            window s[l:r+1]: always contians k number where r - l + 1 = k
            res: contains max value from s[l:r+1]


        """
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output


