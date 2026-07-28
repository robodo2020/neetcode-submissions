class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
                1,2,2,4,5,6,9
                  |
                1           2
                2 4 5 6 9   2
                2 5 6 9     4 5 
                4           
        """
        candidates.sort()
        res = []
        subset = []

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if j >= i + 1 and candidates[j] == candidates[j-1]:
                    continue
                next_total = total + candidates[j]
                if next_total > target:
                    break
                subset.append(candidates[j])
                dfs(j + 1, next_total)
                subset.pop()

        dfs(0,0)
        return res