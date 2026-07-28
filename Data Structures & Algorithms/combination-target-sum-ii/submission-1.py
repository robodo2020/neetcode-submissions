class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [9,2,2,4,6,1,5]
        sort
        [1,2,2,4,5,6,9]
               []
            1                []
          2    2   4  5 6 9
         2 4 5 4 5 5  6 9
        4  5   5
         
        """
        res = []

        subset = []
        candidates.sort()
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i == len(candidates):
                return
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)
        dfs(0, 0)
        return res
    def combinationSum2_og(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [9,2,2,4,6,1,5]
        sort
        [1,2,2,4,5,6,9]
               []
            1                []
          2    2   4  5 6 9
         2 4 5 4 5 5  6 9
        4  5   5
         
        """
        res = []

        subset = []
        candidates.sort()
        def dfs(i, total):
            # base case
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            # include i case
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subset.pop()

            # not include i case
            for j in range(i + 1, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                if total + candidates[j] > target:
                    break
                subset.append(candidates[j])
                dfs(j + 1, total + candidates[j])
                subset.pop()
        dfs(0, 0)
        return res
        

        

        