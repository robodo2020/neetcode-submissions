class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # flattern the list
        mat = []
        for i in matrix:
            for j in i:
                mat.append(j)
        
        l, r = 0, len(mat) - 1
        while l <= r:
            m = (l + r) // 2
            if mat[m] == target:
                return True
            elif mat[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False

