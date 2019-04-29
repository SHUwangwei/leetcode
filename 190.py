class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = bin(n)[2:]
        length = len(n)
        n = (32-length)*'0' + n
        return int(n[::-1], 2)


s =Solution()
print(s.reverseBits(int('00000010100101000001111010011100', 2)))
