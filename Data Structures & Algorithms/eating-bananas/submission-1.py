class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        key: find the minimum k such that canFinish(k) == True
            if canFinish(k) == True, canFinish(k+1) == True
            if canFinish(k) == False, canFinish(k-1) == False
        h >= len(piles)
        upper bound = max(piles)
        lower bound = 1
        
        boundary search problem
        k:    1  2  3  4  5  6 ...
        ok?   F  F  F  T  T  T ...
                      ^ finding this boundary, use l < r
        """
        r = max(piles)
        l = 1
        while l < r:
            m = (l + r) // 2
            cur_h = 0
            for p in piles:
                cur_h += math.ceil(p / m)
            if cur_h <= h: 
                r = m # m is fast, maybe can get slower. meaning canFinish(m) == True, m might be the answer
            else:
                l = m + 1 # m is too slow, must go faster, m cannot be the answer. meaning canFinish(m) = False
        return l
            
