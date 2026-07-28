class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        def dfs(r, c):
            if not ( -1 < r < len(grid) and -1 < c < len(grid[0]) and grid[r][c] == 1):
                return 0
            grid[r][c] = 2
            dirs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            area = 1
            for x, y in dirs:
                area += dfs(x, y)
            return area




        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        return max_area