class Solution:
    def twoCitySchedCost(self, costs):
        length = len(costs)
        N = length // 2
        costs.sort(key=lambda x:abs(x[0]-x[1]), reverse=True)
        city = {
        'A':0,
        'B':0
        }
        amount = 0
        for cost in costs:
            if city['A'] < N and city['B'] < N:

                res = 'A' if cost[0] < cost[1] else 'B'
                amount += cost[0] if res == 'A' else cost[1]
                city[res] += 1
            elif city['A'] == N and city['B'] < N:
                city['B'] += 1
                amount += cost[1]
            else:
                city['A'] += 1
                amount += cost[0]
        return amount


        # costs.sort(key = lambda x:  x[0]-x[1])

        # N = len(costs) // 2
        # cost = 0
        # for i in range(N):
        #     cost += costs[i][0]
        # for i in range(N):
        #     cost += costs[N+i][1]
        # return cost



s = Solution()

print(s.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))

