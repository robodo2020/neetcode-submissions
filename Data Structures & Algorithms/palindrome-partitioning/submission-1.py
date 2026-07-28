class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
                    ababab
                       |
             a    ab      aba     abab      ababa      ababab
           
        cannot figure that out lol, why code is so easy
        """
        res = []
        pal = []
        def is_pal(cur_s, l, r):
            while l < r:
                if cur_s[l] != cur_s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(pal.copy())
                return
            
            for j in range(i, len(s)):
                if is_pal(s, i, j):
                    pal.append(s[i:j+1])
                    dfs(j + 1)
                    pal.pop()
        dfs(0)
        return res

       
