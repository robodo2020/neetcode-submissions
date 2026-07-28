class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        TC: O(n)
        SC: O(1)
        """
        l, r = 0, len(s) - 1
        while l <= r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and r > l:
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

                

        """
        easiest implementation
        """
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]

        """
        first try
        """
        s_clean = ""
        for c in s:
            if c.isalnum():
                s_clean += c.lower()
        l, r = 0, len(s_clean) - 1
        while l <= r:
            if s_clean[l] != s_clean[r]:
                return False
            l += 1
            r -= 1
        return True