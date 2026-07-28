class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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
        for square in range(9):
            seen = set()
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