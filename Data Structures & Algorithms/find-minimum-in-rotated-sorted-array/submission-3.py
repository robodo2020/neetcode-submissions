class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3,4,5,6,1,2]
        invariant: minimum answer always inside [l, r]
        """
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]: # min is in right half
                l = m + 1 # no need to include m, since m is larger
            else: # min is at left half, inlcude m, since m is smaller
                r = m 
        return nums[l]