class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        sorting method
        [9,1,4,7,3,-1,0,5,8,-1,6]
        1. sort first
        [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
        2. consider about consequtive
         - num the same, ignore
         - num differ + 1, conunt streak




        """
        if len(nums) == 0:
            return 0
        nums.sort()
        print(nums)

        current = longest = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                current += 1
            else:
                current = 1
            if current > longest:
                longest = current

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