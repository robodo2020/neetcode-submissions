class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        need to review
        from the 
        """
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visited, pre_height):
            if not (-1 < r < rows and -1 < c < cols):
                return
            if (r, c) in visited or heights[r][c] < pre_height:
                return
            
            visited.add((r, c))
            dirs = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]
            for x, y in dirs:
                dfs(x, y, visited, heights[r][c])
            return
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])
        
        return list(pac & atl)



