class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        XYYX k=2

        invaraint 不變量
        window len -> len
        max freq char -> max_freq
        替換次數 -> len - max_freq

        len - max_freq <= k  
           整題核心
        """
        count = {}
        max_freq = 0
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_freq = max(max_freq, count[s[r]])
            # why doesn't need to update max_freq?
            # eg AAAABBBAAAA k=2
            # when hitting while loop (l=0, r=6), 1. not expanding max_freq
            # 2. basically we just wanted to move ptr l, to know where l should move to
            # 3. worst case, clear the max_freq in count (ex AAAABBB, clear all count for A)
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

            
