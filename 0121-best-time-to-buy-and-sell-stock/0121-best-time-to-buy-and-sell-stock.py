class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice=prices[0]
        income=0
        for i in range(1,len(prices)):
            minPrice=min(minPrice,prices[i])
            income=max(income,prices[i] - minPrice)
        return income
        