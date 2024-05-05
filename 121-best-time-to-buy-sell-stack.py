class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        buy_price = prices[0]
        maxp = 0
        for p in prices[1:]:
            if p < buy_price:
                buy_price = p
            else:
                maxp = max(maxp,p - buy_price)
        return maxp
 