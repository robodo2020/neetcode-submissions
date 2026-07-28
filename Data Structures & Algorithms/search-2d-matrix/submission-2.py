class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        key:
        index = row_idx * col + col_idx
        m = mr * col + mc
        """
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1
        while l <= r:
            m = (l + r) // 2

            mr = m // col 
            mc = m % col
            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] < target:
                l = m + 1
            else:
                r = m - 1
        return False

