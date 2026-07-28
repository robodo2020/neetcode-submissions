class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        sol 1: sorting
        """
        mapping = {}
        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s not in mapping:
                mapping[sorted_s] = []
            mapping[sorted_s].append(s)
        
        res = []
        for k, v in mapping.items():
            res.append(v)
        return res


        
        """
        sol 2: hash table
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
