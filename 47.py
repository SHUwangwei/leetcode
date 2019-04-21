class Solution:
    def permuteUnique(self, nums):
        length = len(nums)
        if length <= 1:
            return [nums]
        self.res = []
        nums.sort()
        self.search(0, length, nums)
        return self.res


        
    def search(self, start, length, nums):
        if start == length:
            #if nums not in self.res:
            self.res.append(nums[:])
            return
        for i in range(start, length):
            if ((i != start and nums[i] == nums[start]) or (i > start and nums[i] == nums[i-1])):
                continue
            nums[i], nums[start] = nums[start], nums[i]
            self.search(start+1, length, nums)
            nums[start], nums[i] = nums[i], nums[start]

s = Solution()

print(s.permuteUnique([1,1,2,2]))