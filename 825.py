#coding = utf-8


class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        import math
        res = {}
        sums = {}
        num = 0
        for age in ages:
            res[age] = res.setdefault(age, 0) + 1
        sums[0] = 0
        for i in range(1, 121):
            sums[i] = res.setdefault(i, 0) + sums[i-1]
        for first in range(15, 121):
            if res.setdefault(first, 0) == 0:
                continue
            second = math.floor(first*0.5+7)
            count = sums[first] - sums[second]
            count -= 1
            count *= res[first]
            num += count
        return num

s = Solution()

res = s.numFriendRequests([20, 30, 100, 110, 120])
print(res)
