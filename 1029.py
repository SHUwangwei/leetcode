class Solution:
    def twoCitySchedCost(self, costs):
        length = len(costs)
        listA = [costs[i][0] for i in range(length)]
        listB = [costs[i][1] for i in range(length)]
        listA.sort()
        listB.sort()
        res = sum(listA[:length//2] + listB[:length//2])
        return res
