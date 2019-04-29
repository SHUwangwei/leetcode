class Solution:
    def titleToNumber(self, s):
        length = len(s)
        if length < 0:
            return 0
        count = 0
        res = 0
        for i in range(length-1, -1, -1):
            res += (26 ** count)*(ord(s[i])-64)
            count += 1
        return res