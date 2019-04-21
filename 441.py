class Solution:
    def arrangeCoins(self, n):
        res = 0
        i = 1
        s = 0
        while True:
            s += i
            if s == n:
                return i
            elif s > n:
                return i-1
            else:
                i += 1


s = Solution()
print(s.arrangeCoins(8))