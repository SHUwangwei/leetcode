
class Solution:
    def baseNeg2(self, N):
        if N == 0:
            return '0'
        res = ''
        while N != 0:
            r = N % (-2)
            N = N // (-2)
            print(r, N)
            if (r < 0):
                N += 1
                r += 2
            res += str(r)
        return res[::-1]

s = Solution()
print(s.baseNeg2(2))