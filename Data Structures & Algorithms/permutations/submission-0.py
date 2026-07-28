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
        nums_set = set(nums)

        def dfs(local_nums):
            if len(nums_set) == 0:
                res.append(perm.copy())
            
            for num in local_nums:
                if num not in nums_set:
                    continue
                nums_set.remove(num)
                perm.append(num)
                dfs(local_nums)
                nums_set.add(num)
                perm.pop()
        dfs(nums)
        return res
        

            