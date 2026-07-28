class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        need to consider if find anything or not
        only if find something, then add time += 1
        """
        rows, cols = len(grid), len(grid[0])
        queue = collections.deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        # while queue and fresh > 0:
        
        while queue:
            n = len(queue)
            print(queue)
            for _ in range(n):
                r, c = queue.popleft()
                dirs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

                for x, y in dirs:
                    if -1 < x < rows and -1 < y < cols and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -=1
                        queue.append((x, y))
            if len(queue) > 0:
                time += 1
        
        return -1 if fresh > 0 else time
