class Solution:
    def longestMountain(self, A):
        length = len(A)
        if length < 3:
            return 0
        dpl = length*[1]
        dpr = length*[0]
        for i in range(1, length):
            if A[i] > A[i-1]:
                dpl[i] = dpl[i-1] + 1
        if A[length-1] < A[length-2]:
            dpr[length-1] = 1
        for i in range(length-2, 0, -1):
            if A[i] < A[i-1]:
                dpr[i] = dpr[i+1] + 1
        ans = 0
        for i in range(0, length-1):
            if dpr[i+1] > 0 and dpl[i] > 1:
                ans = max(ans, dpl[i]+dpr[i+1])
        if ans >= 3:
            return ans
        else:
            return 0


s = Solution()

print(s.longestMountain([9,8,7,6,5,4,3,2,1,0]))
