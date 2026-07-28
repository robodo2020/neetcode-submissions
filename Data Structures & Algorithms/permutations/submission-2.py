class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
            [1,2,3]
            1      2
           2 3   1  3
          3  2  3   1

        {2,3}
        [1]
        [1,2,3]
         |        
        """

        perm = []
        res = []

        def dfs(local_nums):
            if len(local_nums) == 0:
                res.append(perm.copy())
                return
            
            for i, num in enumerate(local_nums):
                perm.append(num)
                next_nums = local_nums[:i] + local_nums[i+1:]
                dfs(next_nums.copy())
                perm.pop()
        dfs(nums)
        return res

    def permute_og(self, nums: List[int]) -> List[List[int]]:
        """
            [1,2,3]
            1      2
           2 3   1  3
          3  2  3   1

        {2,3}
        [1]
        [1,2,3]
         |        
        """

        perm = []
        res = []
        nums_set = set(nums)

        def dfs():
            if len(nums_set) == 0:
                res.append(perm.copy())
            
            for num in nums:
                if num not in nums_set:
                    continue
                nums_set.remove(num)
                perm.append(num)
                dfs()
                nums_set.add(num)
                perm.pop()
        dfs()
        return res
        

            