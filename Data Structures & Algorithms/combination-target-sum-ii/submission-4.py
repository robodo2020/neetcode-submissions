class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
         [1,2,2,4,5,6,9]
              |
        subset = [1,2,2] total = 9
        use the for loop to break continuing finding the next larger number (unnecessary)
        """
        res = []

        subset = []
        candidates.sort()
        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                next_total = total + candidates[j]
                if next_total > target:
                    break
                subset.append(candidates[j])
                dfs(j + 1, next_total)
                subset.pop()
        dfs(0, 0)
        return res

    def combinationSum2_better(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        [9,2,2,4,6,1,5]
        sort
        [1,2,2,4,5,6,9]
              []
        

        cons, didn't stop the traverse the next when the total already over the target
        """
        res = []

        subset = []
        candidates.sort()
        def dfs(i, total):
            # base case
            if total == target:
                res.append(subset.copy())
                return
            if total > target or i == len(candidates):
                return
            
            # include i case
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            subset.pop()

            # exclude i case
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
            # redundant operation tho
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
        

        

        