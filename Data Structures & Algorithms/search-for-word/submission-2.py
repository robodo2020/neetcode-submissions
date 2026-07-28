class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            ["A","B","C","D"],
            ["S","A","A","T"],
            ["A","C","A","E"]
        """
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (-1 < r < len(board) and -1 < c < len(board[0]) and word[i] == board[r][c] and ((r, c) not in visited)):
                return False
            visited.add((r, c))
            res = (dfs(r + 1, c, i + 1) or 
                   dfs(r - 1, c, i + 1) or 
                   dfs(r, c + 1, i + 1) or 
                   dfs(r, c - 1, i + 1))
            visited.remove((r, c))
            return res



        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    res = dfs(r, c, 0)
                    if res:
                        return True
        return False

