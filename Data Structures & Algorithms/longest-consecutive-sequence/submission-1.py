class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            [2,20,4,10,3,4,5]
        num  |
     streak     0

        """
        # brute force
        res = 0
        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1
            res = max(res, current_streak)
        return res
            



        """
        numsSet = set(nums) # each num only will appear once
        result = 0
        for n in nums:
            if n - 1 not in numsSet:
                l = 0 # meaning it's the start point
                while n + l in numsSet: # 
                    l += 1
                result = max(result, l)
        return result
        """