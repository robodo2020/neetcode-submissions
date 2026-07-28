class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        need to review
        from the 
        """
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visit, prev_height):
            if not ( -1 < r < rows and -1 < c < cols):
                return
            if ((r, c) in visit or 
                heights[r][c] < prev_height):
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        """
        we are checking any nodes can reach pacific upwards, so from pacific, 
        we know the first frow can definitely reach pacific, then check the notes that can reach pacific through it
        """
        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) # from the first row, mark all cells that can reach pacific
            dfs(rows - 1, c, atl, heights[rows-1][c]) # from the last row, mark all cell that can reach atlantic
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0]) # from the first column, mark all cells that can reach pacific
            dfs(r, cols - 1, atl, heights[r][cols - 1]) # from the last column, mark all cell that can reach atlantic
        
        
        return list(pac & atl)
            
        


