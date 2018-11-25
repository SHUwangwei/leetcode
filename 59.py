#coding=utf-8


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0]*n for i in range(n)]
        data = (i+1 for i in range(n**2))
        h = n
        w = n
        start = [0, 0]
        while h != 0:
            if h == 1:
                res[start[0]][start[1]] = next(data)
                break
            for i in range(start[1], start[1]+w-1):
                res[start[0]][i] = next(data)
            for i in range(start[0], start[0]+h-1):
                res[i][start[1]+w-1] = next(data)
            for i in range(start[1]+w-1, start[1], -1):
                res[start[0]+h-1][i] = next(data)
            for i in range(start[0]+h-1, start[0], -1):
                res[i][start[1]] = next(data)
            h -= 2
            w -= 2
            start[0] += 1
            start[1] += 1

        return res


s = Solution()
res = s.generateMatrix(3)
print(res)