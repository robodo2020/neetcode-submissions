class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        subset = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res
    def subsetsWithDup_optimize(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        subset = []

        def dfs(i):
            if i == len(nums):
                res.add(tuple(subset))
                return
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return [list(s) for s in res]

    def subsetsWithDup_og(self, nums: List[int]) -> List[List[int]]:
        """
            [1,2,1]
             |          
                         []
                  1                  []
            2         [1]           [2]       []
           1 [1,2]  [1,1] [1]     [1]  [2]   [1] []
        """

        res = []
        subset = []
        dup = set()
        def dfs(local_nums):
            if len(local_nums) == 0:
                t = tuple(sorted(subset)) if subset else ""
                if t not in dup:
                    res.append(subset.copy())
                    dup.add(t)
                    return
            
            for i, num in enumerate(local_nums):
                # include current num
                subset.append(num)
                next_nums = local_nums[:i] + local_nums[i + 1:]
                dfs(next_nums)
                subset.pop()
                # exclude current num
                dfs(next_nums)
            return
        dfs(nums)
        return res

            

