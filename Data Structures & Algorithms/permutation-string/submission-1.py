class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        """
        n, m = len(s1), len(s2)
        if n > m:
            return False
        count1 = collections.defaultdict(int)
        for c in s1:
            count1[c] += 1
        window  = collections.defaultdict(int)
        for i in range(n):
            window[s2[i]] += 1

        if count1 == window:
            return True
        
        l = 0
        for r in range(n, m):
            window[s2[r]] += 1 
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
            l += 1
            if window == count1:
                return True
        return False
