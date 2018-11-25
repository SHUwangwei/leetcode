#coding=utf-8

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        l = 0
        r = 0
        res = 0
        minlength = length+1
        for r in range(length):
            res += nums[r]
            while res >= s:
                minlength = min(minlength, r-l+1)
                res -= nums[l]
                l += 1
        return 0 if minlength == length+1 else minlength
s = Solution()
sums = s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(sums)