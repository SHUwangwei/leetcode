# coding=utf-8
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(candidates)
        candidates.sort()
        res = []
        path = []
        starts = 0
        self.search(candidates, res, path, starts, length, target)
        return res

    def search(self, candidates, res, path, starts, length, target):
        # if starts >= length or target < 0:
        #     return
        if target == 0:
            res.append(list(path))
        elif target < 0:
            return
        begin = starts
        while(starts < length):
            if starts > begin and candidates[starts] == candidates[starts - 1]:
                starts += 1
                continue
            if candidates[starts] > target:
                break
            path.append(candidates[starts])
            self.search(candidates, res, path, starts + 1,
                        length, target - candidates[starts])
            path.pop()
            starts += 1


s = Solution()
res = s.combinationSum2([1, 2, 3, 1, 4], 5)
print(res)
