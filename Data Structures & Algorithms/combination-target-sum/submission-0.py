class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
                2            5   6  9
              2      5     6    9
            2  5    6
          2  5
         2
        """
        nums.sort()
        res = []
        subset = []
        def dfs(i, sum):
            if i >= len(nums) or sum > target:
                return
            if sum == target:
                res.append(subset.copy())
                return
            # take nums[i]
            subset.append(nums[i])
            dfs(i, sum + nums[i])
            subset.pop()

            # skip nums[i], take the next one
            dfs(i + 1, sum)
        dfs(0, 0)
        return res
