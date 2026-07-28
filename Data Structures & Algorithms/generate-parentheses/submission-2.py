class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        invariant:
            0 <= nopen < n
            0 <= nclose <= nopen
        """
        subset = []
        res = []
        def dfs(nopen, nclose):
            if nopen == nclose == n:
                res.append(''.join(subset))
                return
            
            if nopen < n:
                subset.append('(')
                dfs(nopen + 1, nclose)
                subset.pop()
            if nclose < nopen:
                subset.append(')')
                dfs(nopen, nclose + 1)
                subset.pop()
            
        dfs(0, 0)
        return res
    def generateParenthesis_og(self, n: int) -> List[str]:
        """
           n open, n close -> return
           number of close < open, can do everything
            else, only allow to add open
        """
        subset = []
        res = []
        def dfs(nopen, nclose):
            if nopen == nclose == n:
                res.append(''.join(subset))
                return
            if nopen > n or nclose > n:
                return
            
            if nclose < nopen:
                # ( case
                subset.append("(")
                dfs(nopen + 1, nclose)
                subset.pop()

                # ) case
                subset.append(')')
                dfs(nopen, nclose + 1)
                subset.pop()
            else:
                # only allow to add (
                subset.append("(")
                dfs(nopen + 1, nclose)
                subset.pop()
        dfs(0, 0)
        return res


                
            



