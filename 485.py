class Solution:
    def findMaxConsecutiveOnes2(self, nums):
        length = len(nums)
        res = 0
        left = 0
        right = 0
        while(left < length and right < length):
            if nums[left] == 0:
                left += 1
                continue
            right = left
            while(right < length and nums[right] == 1):
                right += 1
            res = max(res, right - left)
            left = right + 1
        return res

    def findMaxConsecutiveOnes(self, nums):
        cur_len = 0
        max = 0
        for num in nums:
            if num == 1:
                cur_len += 1
            elif num == 0:
                if cur_len > max:
                    max = cur_len
                cur_len = 0
        if cur_len > max:
            max = cur_len
        return max
