class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        length = len(S)
        dp = [0] * length
        count = 0 if S[0] == '0' else 1
        for i in range(1, length):
            count += int(S[i])
            dp[i] = min(dp[i-1]+1- int(S[i]), count)
        return dp[length-1]
