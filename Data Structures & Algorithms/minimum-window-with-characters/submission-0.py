class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            OUZODYXAZV
            |
            |
        
        invariant:
        window: s[l:r+1] when meet condition, contain char in t
        """
        
        counts, countt = {}, {}
        for c in t:
            countt[c] = 1 + countt.get(c, 0)
        
        l = 0
        need = 0
        have = len(countt)
        minlen = float("inf")
        minres = ""
        def check_valid():
            for k, v in countt.items():
                if k not in counts or counts[k] < v:
                    return False
            return True
        for r, c in enumerate(s):
            counts[c] = 1 + counts.get(c, 0)

            while check_valid():
                cur_len = r - l + 1
                if cur_len <= minlen:
                    minlen = r - l + 1
                    minres = s[l: r+1]
                
                counts[s[l]] -= 1
                l += 1
        return minres
            

                


