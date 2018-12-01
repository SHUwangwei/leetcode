# coding=utf-8


class Solution:
    def combinationSum(self, candidates, target):
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
        if target == 0:
            res.append(list(path))
        while(starts < length):
            if candidates[starts] > target:
                break
            path.append(candidates[starts])
            self.search(candidates, res, path, starts,
                        length, target - candidates[starts])
            path.pop()
            starts += 1


s = Solution()
res = s.combinationSum([1, 2, 3, 4], 7)
print(res)
