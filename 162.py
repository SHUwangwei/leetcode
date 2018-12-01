#coding=utf-8

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left = 0
        right = length-1
        while(left <= right):
            if left == right:
                return left
            center = (left+right)//2
            if nums[center] < nums[center+1]:
                left = center+1
            else:
                right = center
s = Solution()
res = s.findPeakElement([1,2,3,1])
print(res)