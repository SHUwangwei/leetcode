class Solution:
    def camelMatch2(self, queries, pattern):
        import re
        newpattern = '^([a-z\s]*?)'
        for p in pattern:
            newpattern += p+'([a-z\s]*?)'
        newpattern += '$'
        res = []
        for query in queries:
            match = re.search(newpattern, query)
            if match:
                res.append(True)
            else:
                res.append(False)
        return res
    def camelMatch(self, queries, pattern):
        ans = list()
        l = len(pattern)

        for query in queries:
            pos = 0
            flag = True

            for ch in query:
                if pos < l and ch == pattern[pos]:
                    pos += 1
                else:
                    if "A" <= ch <= "Z":
                        flag = False
                        break
            if pos < l:
                flag = False
            ans.append(flag)
        return ans


s = Solution()
s.camelMatch([], 'FB')