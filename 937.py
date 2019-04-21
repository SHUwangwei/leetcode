class Solution:

    def reorderLogFiles(self, logs):
        # from functools import cmp_to_key
        # def cmp(log1, log2):
        #     if log1.split(' ', 1)[1] < log2.split(' ', 1)[1]:
        #         return -1
        #     else:
        #         return 1

        res_digit = []
        res_alpha = []
        for log in logs:
            if log.split(' ')[1][0].isalpha():
                res_alpha.append(log)
            else:
                res_digit.append(log)
        print(res_alpha)
        res_alpha = sorted(res_alpha, key=lambda item: item.split(' ', 1)[1])
        res_alpha.extend(res_digit)

        return res_alpha

    
s = Solution()
print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))