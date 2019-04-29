class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x
        
class Solution:
    def largestNumber2(self, nums):
        from functools import cmp_to_key
        def cmp(a, b):
            if len(a) == len(b):
                return 1 if a < b else -1
            elif a[0] != b[0]:
                return 1 if a[0] < b[0] else -1
            else:
                return -1 if a+b > b+a else 1
        length = len(nums)
        if nums == [0]*length:
            return '0'
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(cmp))
        return ''.join(nums)
        
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num
