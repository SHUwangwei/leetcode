# coding=utf-8


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from functools import reduce

        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 0:
            return 0
        temp = 1
        left = []
        for i in nums:
            temp *= i
            left.append(temp)
        temp = 1
        right = []
        for i in nums[-1: :-1]:
            temp *= i
            right.append(temp)
        right.reverse()
        res = []
        for i in range(1, length-1):
            res.append(left[i-1]*right[i+1])
        print(left)
        print(right)
        res.append(left[length-2])
        res.insert(0, right[1])
        return res

s = Solution()
res = s.productExceptSelf([1, 3, 5, 7])
print(res)
