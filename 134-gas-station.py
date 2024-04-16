class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        total_gas = 0
        start_city = 0
        current_gas = 0
        for i in range(n):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                start_city = i + 1
                current_gas = 0

        if total_gas < 0:
            return -1
        else:
            return start_city
        