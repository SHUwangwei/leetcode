# coding=utf-8


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        length = len(nums)
        res = []
        for i in range(length):
            self.search(i, length, res, nums, k)
        return len(res)
    def search(self, start, ends, res, nums, k):
        #res.append(list(temp))
        from functools import reduce
        temp = []
        if (start != 0 and nums[start-1] == nums[start]):
            temp.append(nums[start])
            while(start < ends-1 and nums[start] == nums[start+1]):
                temp.append(nums[start])
                start += 1
            start += 1
        for i in range(start, ends):
            temp.append(nums[i])
            if reduce(lambda x, y: x*y, temp) < k:
                res.append(list(temp))
                print(temp)
            else:
                return


s = Solution()
res = s.numSubarrayProductLessThanK([1, 1, 1, 2], 23)
print(res)


