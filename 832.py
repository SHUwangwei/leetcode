# coding=utf-8


class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for index, row in enumerate(A):
            row.reverse()
            #row = list(map(lambda x: x ^ 1, row))
            A[index] = list(map(lambda x: x ^ 1, row))
        return A


s = Solution()
res = s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
print(res)