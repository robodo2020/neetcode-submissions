class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        345
        mapping
        3: 'def'
        4: 'gfi'
        5: 'jkl'
          d
         g
        j k
        
        """
        if not digits:
            return []
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []

        def dfs(i, cur_str):
            if i == len(digits):
                res.append(cur_str)
                return
            cur_number = digits[i]

            for c in mapping[cur_number]:
                dfs(i + 1, cur_str + c) 
                # directly add the string, the after dfs it will remove the last char automatically
        dfs(0, '')
        return res


    def letterCombinations_og(self, digits: str) -> List[str]:
        """
        345
        mapping
        3: 'def'
        4: 'gfi'
        5: 'jkl'
          d
         g
        j k
        
        """
        if not digits:
            return []
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []
        subset = []

        def dfs(i):
            if len(subset) == len(digits):
                res.append(''.join(subset))
                return
            cur_number = digits[i]

            for c in mapping[cur_number]:
                subset.append(c)
                dfs(i + 1)
                subset.pop()
        dfs(0)
        return res





