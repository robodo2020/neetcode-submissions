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
            if not (-1 < r < len(board) and -1 < c < len(board[0])):
                return False
            if (r, c) in visited:
                return False
            if board[r][c] != word[i]:
                return False
            visited.add((r, c))
                
            dirs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for x, y in dirs:
                if dfs(x, y, i + 1):
                    return True
            visited.remove((r, c))
            return False



        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    res = dfs(r, c, 0)
                    if res:
                        return True
        return False

