class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i=0
        j=1
        maxi=0
        while j<len(prices):
            if prices[i]<prices[j]:
                profit=prices[j]-prices[i]
                maxi=max(maxi,profit)
            else:
                i=j
            j+=1
        return maxi