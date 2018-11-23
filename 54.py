#coding=utf-8


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        m_left = m
        n_left = n
        left_top = [0, 0]
        right_top = [0, n-1]
        left_bottom = [m-1, 0]
        right_bottom = [m-1, n-1]
        res = []
        while True:
            if m_left <= 1 or n_left <= 1:
                if m_left == 1:
                    temp = left_top[0]
                    for i in range(left_top[1], right_top[1]+1):
                        res.append(matrix[temp][i])
                elif n_left == 1:
                    temp = left_top[1]
                    for i in range(left_top[0], left_bottom[0]+1):
                        res.append(matrix[i][temp])
                break
            temp = left_top[0]
            for i in range(left_top[1], right_top[1]):
                res.append(matrix[temp][i])
            temp = right_top[1]
            for i in range(right_top[0], right_bottom[0]):
                res.append(matrix[i][temp])
            temp = right_bottom[0]
            for i in range(right_bottom[1], left_bottom[1], -1):
                res.append(matrix[temp][i])
            temp = left_bottom[1]
            for i in range(left_bottom[0], left_top[0], -1):
                res.append(matrix[i][temp])
            m_left -= 2
            n_left -= 2
            left_top[0] += 1
            left_top[1] += 1
            left_bottom[0] -= 1
            left_bottom[1] += 1
            right_top[0] += 1
            right_top[1] -= 1
            right_bottom[0] -= 1
            right_bottom[1] -= 1
        return res


s = Solution()
#print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
