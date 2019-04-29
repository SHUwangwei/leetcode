class Solution:
    def isHappy(self, n):
        resset = set()
        resset.add(n)
        while(n != 1):

            n = self.getlist(n)
            if n not in resset:
                resset.add(n)
            else:
                return False
        return True


    def getlist(self, n):
        res = 0
        while(n != 0):
            # n, y = divmod(n, 10)
            # res += y**2
            y = n%10
            n //= 10
            res += y**2
        return res