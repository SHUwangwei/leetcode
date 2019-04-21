class Solution:
    def rob(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums)
        res = [0] * length
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        for i in range(2, length):
            res[i] = max(res[i-2]+nums[i], res[i-1])
        # length = len(nums)
        # if length == 0:
        #     return 0
        # res = length * [0]
        # for i in range(0, length):
        #     res[i] = max((res[i - 2] if i > 1 else 0) +
        #                  nums[i], (res[i - 1] if i > 0 else 0))
        return res[-1]
