#coding=utf-8

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        res = []
        path = []
        starts = 0
        self.search(nums, res, path, starts, length)
        res.append([])
        return res

    def search(self, nums, res, path, starts, length):
            if starts >= length:
                return
            while(starts < length):
                path.append(nums[starts])
                res.append(list(path))
                self.search(nums, res, path, starts+1, length)
                path.pop()
                starts += 1
s = Solution()
print(s.subsets([1, 2, 3, 4]))
