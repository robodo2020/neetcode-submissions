class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [30,38,30,36,35,40,28]
         |
         if any future day weather is higher, track this
         [38,36,35]
         40
        [1,0,1,0,0,0,0]
        invariant
        stack: store all index that in a decreasing order of tem[i]

        """
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res


        