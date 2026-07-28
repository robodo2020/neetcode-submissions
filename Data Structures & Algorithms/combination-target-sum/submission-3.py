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
            
            # since it's already too big, and it's sorted not worth to keep checking the next element
            if sum + nums[i] > target:
                return
            # take nums[i]
            subset.append(nums[i])
            dfs(i, sum + nums[i])
            subset.pop()

            # skip nums[i], go check the next one
            # prob will use it, or skip it, use the next recursion to determine
            dfs(i + 1, sum)
        dfs(0, 0)
        return res
