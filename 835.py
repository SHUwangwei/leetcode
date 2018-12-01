# coding=utf-8


class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        n = len(A)
        res = 0
        for a in range(-n + 1, n):
            for b in range(-n + 1, n):
                count = 0
                for rowindex in range(-a, n - a):
                    for colindex in range(-b, n - b):
                        if rowindex >= 0 and rowindex < n and colindex < n and \
                                colindex >= 0 and B[rowindex + a][colindex + b] == 1 and A[rowindex][colindex] == 1:
                            count += 1
                if count > res:
                    res = count
                    pos = (a, b)
        print(pos)
        return res


s = Solution()
A = [[1, 1, 0], [0, 1, 0], [0, 1, 0]]
B = [[0, 0, 0], [0, 1, 1], [0, 0, 1]]
res = s.largestOverlap(A, B)
print(res)