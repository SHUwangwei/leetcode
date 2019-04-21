class Solution:
    def coinChange(self, coins, amount):
        length = len(coins)
        coin_result = [float('inf')]*(amount+1)
        coin_result[0] = 0
        for coin in coins:
            for val in range(coin, amount+1):
                coin_result[val] = min(coin_result[val], coin_result[val-coin]+1)
        if coin_result[-1] == float('inf'):
            return -1
        else:
            return coin_result[-1]














print(3)
s = Solution()
print(s.coinChange([1,2,5], 11))
