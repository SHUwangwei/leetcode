#coding=utf8

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        res = []
        path = []
        starts = 0
        nums.sort()
        self.search(nums, res, path, starts, length)
        res.append([])
        return res


    def search(self, nums, res, path, starts, length):

        if starts >= length:
            return
        origin = starts
        while(starts < length):

            if starts > origin and nums[starts] == nums[starts-1]:
                starts += 1
                continue
            path.append(nums[starts])
            #print(path)
            res.append(list(path))
            #print(res)
            self.search(nums, res, path, starts+1, length)

            path.pop()

            starts += 1

s = Solution()
print(s.subsetsWithDup([1,2,2,2,3]))