class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        having prefix & postfix to multiple
        bascially, for each element, just want all value before it, and after it, to multiple
        multify every value from left to right, and right to left
                 [1,2,3,4]
        prefix  1[1,2,6,24]  --> [1,1,2,6,24]
        postfix  [24,24,12,4]1 ->[24,24,12,4,1]

        to get each result, just take prefix i-1, and postfix 1+1, multiple together and can get answer
        output  [24, 12, 8, 6]
        """
        prefix = []
        postfix = []
        pre = 1
        prefix.append(1)
        for num in nums:
            pre *= num
            prefix.append(pre)
        
        post = 1
        for num in reversed(nums):
            post *= num
            postfix.insert(0, post)
        postfix.append(1)
        
        res = []
        for i in range(len(prefix) - 1):
            val = prefix[i] * postfix[i + 1]
            res.append(val)
        return res

        

