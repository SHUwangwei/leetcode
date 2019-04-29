class Solution:
    def isPalindrome(self, s):
        s2 = ''
        for ss in s:
            if ss.isalnum():
                s2 += ss.lower()
        return s2 == s2[::-1]

s = Solution()

print(s.isPalindrome("A man, a plan, a canal: Panama"))


        