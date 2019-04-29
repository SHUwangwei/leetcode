class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        c = Counter(nums)
        c = c.most_common(k)
        return [item[0] for item in c]