class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        bucket = [0] * 26
        for i in range(len(s)):
            bucket[ord(s[i]) - ord('a')] += 1
            bucket[ord(t[i]) - ord('a')] -= 1
        
        for n in bucket:
            if n != 0:
                return False
        return True
        

