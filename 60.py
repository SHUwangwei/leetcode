class Solution:
    def getPermutation(self, n, k):
        import math
        res = ''
        res_list = [str(i) for i in range(1, n+1)]
        if n == 1:
            return '1'
        v_base = math.factorial(n-1)
        for i in range(n-1, 0, -1):
            print(v_base)
            count = math.ceil(k/v_base)
            k %= v_base

            if count > 0:
                res += res_list[count-1]
                del res_list[count-1]
            else:
                res += res_list.pop(0)
            v_base //= i
            if k == 0:
                res_list.reverse()
                res += ''.join(res_list)
                break
        #res += res_list[0]
        return res

s = Solution()
print(s.getPermutation(3, 2))