class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        optimize solution:
        """
        num_set = set(nums) # making each num only appears once

        res = 0
        for num in nums:
            if num - 1 not in num_set:
                l = 1 # meaning it's the starting point
                n = num
                while n + 1 in num_set:
                    l += 1
                    n += 1
                res = max(l, res)
        return res
        """
        sorting method
        [9,1,4,7,3,-1,0,5,8,-1,6]
        1. sort first
        [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
        2. consider about consequtive
         - num the same, ignore
         - num differ + 1, count current streak += 1
         - num totally different, current streak reset to 1
        
        TC: O(nlogn)
        SC: O(1)
        """
        if len(nums) == 0:
            return 0
        
        nums.sort()
        current = longest = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                current = 1
            
            longest = max(longest, current)
        return longest


        """
        brute force
        TC: O(n^3)
        SC: O(1)
        """
        res = 0
        for num in nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in nums:
                current_num += 1
                current_streak += 1
            res = max(res, current_streak)
        return res
            



        