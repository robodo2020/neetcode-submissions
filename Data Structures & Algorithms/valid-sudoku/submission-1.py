class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            optimized
        """
        cols = collections.defaultdict(set) # 9 cols
        rows = collections.defaultdict(set) # 9 rows
        squares = collections.defaultdict(set) # 9 squares
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True

        # cols = defaultdict(set)
        # rows = defaultdict(set)
        # squares = defaultdict(set)

        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue
        #         if ( board[r][c] in rows[r]
        #             or board[r][c] in cols[c]
        #             or board[r][c] in squares[(r // 3, c // 3)]):
        #             return False

        #         cols[c].add(board[r][c])
        #         rows[r].add(board[r][c])
        #         squares[(r // 3, c // 3)].add(board[r][c])




        """
        check horizontal
        check vertical
        check 9
        """
        # check horizontal
        for row in board:
            elements = set()
            for ele in row:
                if ele == ".":
                    continue
                if ele in elements:
                    return False
                elements.add(ele)
        
        # check vertical
        for i in range(len(board[0])):
            elements = set()
            for j in range(len(board)):
                ele = board[j][i]
                if ele == ".":
                    continue
                if ele in elements:
                    return False
                elements.add(ele)
        
        # check 9 column
        """
        [0,0] [0,1] [0,2]    [0,3] [0,4] [0,5]
        [1,0] [1,1] [1,2] -> [1,3] [1,4] [1,5]
        [2,0] [2,1] [2,2]    [2,3] [2,4] [2,5]
        """
        # loop each square
        for square in range(9):
            seen = set()
            # loop each square element
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j 
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True