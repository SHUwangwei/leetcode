class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        length = len(ratings)
        if length == 0:
            return 0
        elif length == 1:
            return 1
        candy_result = [1]*length
        for i in range(1, length):
            if ratings[i] > ratings[i-1]:
                candy_result[i] = candy_result[i-1] + 1
        print(candy_result)
        for i in range(length-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if candy_result[i+1] + 1 > candy_result[i]:
                    candy_result[i] = candy_result[i+1] + 1

        print(candy_result)
        return sum(candy_result)
s = Solution()

s.candy([1, 2, 2, 3, 3, 3, 2, 5])