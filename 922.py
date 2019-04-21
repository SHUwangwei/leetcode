#coding=utf-8

class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        length = len(A)
        res = [0]*length
        odd = 1
        even = 0
        for val in A:
            if val % 2 == 0:
                res[even] = val
                even += 2
            else:
                res[odd] = val
                odd += 2
        return res

s = Solution()
res = s.sortArrayByParityII([4, 2, 5, 7])
print(res)
