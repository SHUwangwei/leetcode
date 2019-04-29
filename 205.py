class Solution:
    def isIsomorphic(self, s, t):
        from collections import Counter
        c1 = Counter(s)
        c2 = Counter(t)
        res1 = ''
        res2 = ''
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                res1 += str(count)
                count = 1
        count = 1
        for i in range(1, len(t)):
            if t[i] == t[i-1]:
                count += 1
            else:
                res2 += str(count)
                count = 1



        return list(c1.values()) == list(c2.values()) and res1 == res2