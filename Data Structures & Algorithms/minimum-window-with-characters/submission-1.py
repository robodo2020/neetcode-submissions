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
        have = 0
        need = len(countt)
        minlen = float("inf")
        minres = ""
       
        for r, c in enumerate(s):
            counts[c] = 1 + counts.get(c, 0)

            if c in countt and countt[c] == counts[c]:
                have += 1
            while need == have:
                cur_len = r - l + 1
                if cur_len <= minlen:
                    minlen = r - l + 1
                    minres = s[l: r+1]
                
                counts[s[l]] -= 1
                if s[l] in countt and countt[s[l]] - 1 == counts[s[l]]:
                    have -= 1
                l += 1
        return minres
            

                


