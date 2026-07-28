class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            1,2,3
        each element have two choices, whether to add it, or not to add it

        res = [[1,2,3], [1,2]]
        dfs(0)
                       []
              [1]                []
        [1,2]        [1]       [2]      []
    [1,2,3] [1,2] [1,3] [1] [2,3] [2]  [3] []

        TC: O(n * 2^n)

        SC: O(n + 2^n) = O(2^n)
        """
        
        res = []

        subset = []
        def dfs(i):
            """
                i: the index of the element to add
            """
            if i >= len(nums):
                res.append(subset.copy())
                return

            # to add this value in
            subset.append(nums[i])
            dfs(i + 1)

            # to not add this value in
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res