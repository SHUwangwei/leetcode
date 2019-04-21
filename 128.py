class Solution:
    def longestConsecutive(self, nums):
        hash_table = {}
        length = len(nums)
        maxlength = float('-inf')
        if length == 0:
            return
        for num in nums:
            hash_table[num] = False
        for index, num in enumerate(nums):
            if hash_table.get(num) == True:
                continue
            result = 1
            hash_table[num] = True
            value = num + 1
            while(True):
                if value not in hash_table:
                    break
                else:
                    result += 1
                    hash_table[value] = True
                    value += 1
            value = num - 1
            while(True):
                if value not in hash_table:
                    break
                else:
                    result += 1
                    hash_table[value] = True
                    value -= 1
            if result > maxlength:
                maxlength = result
        return maxlength


s = Solution()

res = s.longestConsecutive([1, 3, 4, 5])
print(res)
print(1)
