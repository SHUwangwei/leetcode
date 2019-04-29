class Solution:
    def knightProbability(self, N, K, r, c):
        dp = [[0]*N for i in range(N)]
        dp[r][c] = 1
        moves = [[-2, -1],[-1, -2], [1, -2], [2, -1], [-2, 1], [-1, 2],[1, 2], [2, 1]]
        for m in range(K):
            dp0 = [[0]*N for i in range(N)]
            for i in range(N):
                for j in range(N):
                    for move in moves:
                        x = i + move[0]
                        y = j + move[1]
                        if x < 0 or y < 0 or x > N-1 or y > N-1:
                            continue
                        dp0[x][y] += dp[i][j]
            dp0, dp = dp, dp0
        res = sum(map(sum, dp))
        return float(res/(8**K))

