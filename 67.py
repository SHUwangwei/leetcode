class Solution:
    def addBinary(self, a, b):
        res = []
        lengtha = len(a)
        lengthb = len(b)
        if lengtha < lengthb:
            a, b = b, a
            lengtha, lengthb = lengthb, lengtha
        jinwei = 0
        for i in range(-1, -1-lengthb, -1):
            r = int(a[i]) + int(b[i]) + jinwei
            t = r % 2
            jinwei = r//2
            res.append(t)
        for i in range(-1-lengthb, -1-lengtha, -1):
            r = int(a[i]) + jinwei
            t = r % 2
            jinwei = r // 2
            res.append(t)
        if jinwei == 1:
            res.append(1)
        return ''.join([str(s) for s in list(reversed(res))])

s = Solution()

print(s.addBinary('1', '111'))





