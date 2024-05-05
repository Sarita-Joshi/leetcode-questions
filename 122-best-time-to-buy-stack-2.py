class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_prof = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            p = prices[i]
            if p > buy:
                curr_prof = max(curr_prof, curr_prof + p-buy)
                buy = p
            elif p < prices[i-1]:
                buy = p
        return curr_prof
                
