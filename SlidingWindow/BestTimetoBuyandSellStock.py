# 121. Best Time to Buy and Sell Stock

def maxProfit(prices):
    buy, sell = 0, 1
    maximumProfit = 0
    while sell < len(prices):
        if prices[sell] > prices[buy]:
            profit = prices[sell] - prices[buy]
            maximumProfit = max(profit, maximumProfit)
        else:
            buy = sell
        sell += 1
    return maximumProfit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
