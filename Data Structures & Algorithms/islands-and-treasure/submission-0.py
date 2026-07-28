class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
            [x,-1,0,x],
            [x,x,x,-1],
            [x,-1,x,-1],
            [0,-1,x,x]

            traverse from 0, 
            if -1, cannot go
            if >0 go -> if points > cur, overwrite
        """

        def dfs(r, c, d):
            if not (-1 < r < len(grid) and -1 < c < len(grid[0])) or grid[r][c] == -1:
                return
            if grid[r][c] < d:
                return
            grid[r][c] = d
            dirs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for x, y in dirs:
                    dfs(x, y, d+1)
            return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
        
