class Solution:
    def letterCasePermutation(self, S):
        str_list = list(S)
        res = []
        for index, s in enumerate(S):
            if s.isalpha():
                str_list2 = str_list[:]
                if len(res) == 0:
                    str_list2[index] = s.upper()
                    res.append(''.join(str_list2))
                    str_list2[index] = s.lower()
                    res.append(''.join(str_list2))
                else:
                    
                    if s.islower():
                        replace_s = s.upper()
                    else:
                        replace_s = s.lower()
                    for r in res[:]:
                        str_list3 = list(r)
                        str_list3[index] = replace_s
                        res.append(''.join(str_list3))
        return res if len(res) else [S]
# class Solution:
#     def letterCasePermutation(self, S):
#         words = list(S)
#         res = ['']
#         'a'.capitalize()
#         while words:
#             last = words.pop()
#             if last.isalpha():
#                 res = [last.lower() + r for r in res] + [last.upper() + r for r in res]
#             else:
#                 res = [last + r for r in res]
#         return res

# s = Solution()

# print(s.letterCasePermutation("a1b2"))
#         
