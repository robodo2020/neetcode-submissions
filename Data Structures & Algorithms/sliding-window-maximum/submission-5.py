class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        [1,2,1,0,4,2,6]
         |
             |
        invariant1: deque has increasing indices
            dq[0] < dq[1] < dq[2]...
        invariant2: deque has decreasing values
            nums[dq[0]] >= nums[dq[1]] >= nums[dq[2]]
        which leads to
            leftmost is 
                the index of the oldest candidate still in the window AND
                the index is the largest value in the window
        """
        dq = deque()
        res = []
        for i, x in enumerate(nums):
            # pop from the right, while cur val >= last val in the deque
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            
            # append the cur idx to deque
            dq.append(i)

            # pop the first item out if it's out of the window range
            if dq[0] <= i - k:
                dq.popleft()
            
            # once we processed at least k elements, now, the head of deque is the max of cur window
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res


