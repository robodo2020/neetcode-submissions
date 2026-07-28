class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        bfs
        """
        count = 0
        def bfs(r, c):
            queue = collections.deque()
            queue.append((r, c))
            
            while queue:
                i, j = queue.popleft()
                grid[i][j] = "#"
                dirs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for x, y in dirs:
                    if -1 < x < len(grid) and -1 < y < len(grid[0]) and grid[x][y] == "1":
                        queue.append((x, y))
                        
            return
        

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    bfs(r, c)
                    count += 1
        return count



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