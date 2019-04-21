# coding=utf-8


class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        length = len(A)
        if length < 3:
            return False
        if A[length-2] <= A[length-1] or A[0] >= A[1]:
            return False
        i = 0
        while(A[i] < A[i + 1]):
            i += 1
        pre = A[i]
        for a in A[i+1:]:
            if a >= pre:
                return False
            else:
                pre = a
        return True
s = Solution()
res = s.validMountainArray([5, 4, 3, 1])
print(res)
