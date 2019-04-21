class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        if length <= 1:
            return 
        for i in range(0, length//2):
            s[i], s[length-1-i] = s[length-1-i], s[i]
        print(s)

s = Solution()
s.reverseString(["H","a","n","n","a","h"])