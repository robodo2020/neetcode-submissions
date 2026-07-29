class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_p = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            max_p = max(max_p, prices[r] - prices[l])
            r += 1
        return max_p


        """
        sliding window 1
        [10,2,5,1,7,1]
     l          |
     r            |
        """
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_profit
        


        """
        sliding window 2
        """
        l = 0
        max_profit = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit

        """
        improvement: DP
        [10,1,5,6,7,1]
        running minimum
        check pre solution to find the best one
        O(1)
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

        