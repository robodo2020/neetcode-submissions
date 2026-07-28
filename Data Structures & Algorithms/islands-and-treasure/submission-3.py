class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        optimize, can traverse both 0 (treasure) node in parallel
        """
        rows, cols = len(grid), len(grid[0])
        inf = 2147483647
        
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        count = 1
        while queue:
            n = len(queue)
            for _ in range(n):
                x, y = queue.popleft()
                dirs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                for i, j in dirs:
                    if -1 < i < rows and -1 < j < cols and grid[i][j] == inf:
                        # grid[x][y] == inf can see as never visit
                        # and the first time visit is always the closest distance
                        queue.append((i, j))
                        grid[i][j] = count
            count += 1
        
            
    def islandsAndTreasure_og(self, grid: List[List[int]]) -> None:
        """
            [x,-1,0,x],
            [x,x,x,-1],
            [x,-1,x,-1],
            [0,-1,x,x]

            traverse from 0, 
            if -1, cannot go
            if >0 go -> if points > cur, overwrite
        """
        

        def bfs(r, c):
            """
            first solution, but doing redundant traverse
            """
            queue = collections.deque()
            queue.append((r, c, 0))
            while queue:
                x, y, d = queue.popleft()
                if not (-1 < x < len(grid) and -1 < y < len(grid[0])) or grid[x][y] == -1:
                    continue
                if grid[x][y] < d:
                    continue
                grid[x][y] = d
                dirs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                for i, j in dirs:
                    queue.append((i, j, d + 1))
            return 

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
                    # dfs(r, c, 0)
                    bfs(r, c)
        
