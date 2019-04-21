#coding=utf-8

class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        flag = False
        maxdistance = 0
        left = 0
        for index, seat in enumerate(seats):
            if flag:
                if seat == 1:
                    maxdistance = max(maxdistance, (index-left)//2)
                    left = index
                else:
                    continue
            else:
                if seat == 1:
                    flag = True
                    maxdistance = max(maxdistance, index)
                    left = index
                else:
                    continue
        maxdistance = max(maxdistance, index-left)
        return maxdistance
s = Solution()
res = s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1])
print(res)
