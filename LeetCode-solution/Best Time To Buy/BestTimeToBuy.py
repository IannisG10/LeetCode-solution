class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # do itteration to find the best day to buy stock
        # begin with the firt stock and looking for a day when the stock is         cheapest 
        stock = prices[0]
        max_profit = 0 
        for i in range(1,len(prices)):
            #verify if the current day is cheap than last day,then buy a stock
            if prices[i] < stock :
                stock = prices[i]
            #find the profit 
            elif prices[i] - stock > max_profit:
                max_profit = prices[i] - stock

        return max_profit

