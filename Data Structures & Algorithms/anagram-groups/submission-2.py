class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        key: val
        [] bucket -> tuple
        val: the str
        """
        mapping = {}
        for s in strs:
            bucket = [0] * 26
            for c in s:
                bucket[ord(c) - ord('a')] += 1
            
            key = tuple(bucket)
            if key not in mapping:
                mapping[key] = []
            mapping[key].append(s)
        
        result = []
        for key, val in mapping.items():
            result.append(val)
        return result
