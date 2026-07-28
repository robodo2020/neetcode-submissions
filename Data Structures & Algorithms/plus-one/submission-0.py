class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for d in digits:
            n = n * 10 + d
        
        n += 1 # int 1235
        res = []
        while n > 0:
            d = n % 10
            res.append(d)
            n = n // 10
        return res[::-1]