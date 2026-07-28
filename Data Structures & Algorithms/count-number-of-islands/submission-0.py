class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        dfs
        """
        count = 0
        def dfs(r, c):
            if -1 < r < len(grid) and -1 < c < len(grid[0]) and grid[r][c] == "1":
                grid[r][c] = "#"
                dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for i, j in dirs:
                    dfs(i, j)
        
                
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        return count