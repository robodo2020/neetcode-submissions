class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [10,1,5,6,7,1]
                  |
    
        brute
        """
        max_res = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                cur_profit = prices[j] - prices[i]
                max_res = max(max_res, cur_profit)
        return max_res

