class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_profit = 0
        min_price = prices[0]

        for price in prices:
            # Update the minimum price if a lower price is encountered
            if price < min_price:
                min_price = price
            # Calculate and update the maximum profit if selling at the current price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
