class Solution:
    def longestOnes(self, A, K):
        length = len(A)
        zero = 0
        left = 0
        right = 0
        res = 0
        while(right < length):
            if A[right] == 0:
                zero += 1
            while zero > K:
                if A[left] == 0:
                    zero -= 1
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res
        