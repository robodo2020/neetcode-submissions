class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        [1,2,1,0,4,2,6]
         |
             |
        invariant:
            window s[l:r+1]: always contians k number where r - l + 1 = k

        
        return the max of each window
        """
        res = []
        for l in range(len(nums) - k + 1):
            cur_max = float("-inf")
            for r in range(l, l + k):
                cur_max = max(cur_max, nums[r])
            
            res.append(cur_max)
        return res



