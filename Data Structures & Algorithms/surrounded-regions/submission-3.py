class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        only need to check the elements in the middle
        surrounded -> any chance to each the edge
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r, c, cur_visited):
            if not (-1 < r < rows and -1 < c < cols):
                return False
            if board[r][c] == 'X':
                return True
            dirs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            cur_visited.add((r, c))
            for x, y in dirs:
                if (x, y) not in cur_visited and (x, y) not in visited:
                    if not dfs(x, y, cur_visited):
                        return False
            return True


        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                cur_visited = set()
                if (r, c) not in visited and board[r][c] == "O" and dfs(r, c, cur_visited):
                    # change all cur_visted to O
                    for (x, y) in cur_visited:
                        board[x][y] = 'X'
                        # add them to visited
                        visited.add((x, y))
        return
        
