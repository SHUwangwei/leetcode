class Solution:
    def canCompleteCircuit2(self, gas, cost):
        length = len(cost)
        add = [gas[i] - cost[i] for i in range(length)]
        i = 0
        count = 0
        while i < length:
            count += 1
            if count > length:
                return -1
            if add[i] < 0:
                i += 1
                continue
            amount = 0
            flag = True
            for j in range(i - length, i):
                amount += add[j]
                if amount < 0:
                    i = j + 1 if j > 0 else j + length + 1
                    flag = False
                    break
            if flag is True:
                return i
        return -1

    def canCompleteCircuit(self, gas, cost):
        if not len(gas) or not len(cost) or len(gas) != len(cost):
            return -1

        tank = 0
        total = 0
        start = 0

        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            if tank < 0:
                start = i + 1
                total += tank
                tank = 0

        if total + tank < 0:
            return -1
        else:
            return start
