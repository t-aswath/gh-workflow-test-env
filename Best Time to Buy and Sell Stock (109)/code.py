class Solution:
    def canAchieveDivisibleProfit(self, prices, k):
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit % k == 0 if max_profit > 0 else False

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        prices = list(map(int, input().split()))
        k = int(input())
        solution = Solution()
        print(solution.canAchieveDivisibleProfit(prices, k))
