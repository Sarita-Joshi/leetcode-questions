class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        if sum(gas) < sum(cost): return -1
        
        startCity = 0 
        totalGas = 0
        for i in range(len(gas)):
            totalGas += gas[i]
            if totalGas < cost[i]:
                startCity = i+1
                totalGas=0
            else:
                totalGas -= cost[i]
            
        
        if startCity >= len(gas):
            return -1
        
        return startCity
        