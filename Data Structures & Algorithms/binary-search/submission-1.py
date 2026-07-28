class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [-1,0,2,4,6,8,10]
              |
              |
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # from aove, already know that nums[m] is not target, no need to include this anymore
            # so that r & l can exclude that
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1


        