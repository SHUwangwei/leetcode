class Solution(object):
    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)[2:]
        return n.count('1')

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while n>0:
            
            ans+=n&1
            n>>=1
        return ans