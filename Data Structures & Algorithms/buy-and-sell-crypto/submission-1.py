class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        improvement
        """
        cur_min = float("inf")
        res = 0
        for p in prices:
            cur_min = min(p, cur_min)
            res = max(res, p - cur_min)
        return res
        

        """
        [10,1,5,6,7,1]
                  |
    
        brute O(n^2)
        """
        max_res = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                cur_profit = prices[j] - prices[i]
                max_res = max(max_res, cur_profit)
        return max_res

        