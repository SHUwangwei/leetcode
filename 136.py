#coding=utf-8

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        res = 0
        for i in range(length):
            res = res ^ nums[i]

        return res


        
s = Solution()

print(s.singleNumber([1, 2, 2, 1, 5]))
