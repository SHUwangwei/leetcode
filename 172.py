class Solution:
    def trailingZeroes(self, n):
        if n <= 0:
             return 0
        res = 0
        while n >= 5:
            n = n // 5
            res += n
        return res

s = Solution()
print(s.trailingZeroes(50))