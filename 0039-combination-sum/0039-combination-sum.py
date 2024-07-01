class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        
        def backtrack(curSum, curList):
            if curSum == target:
                res.add(tuple(sorted(curList)))
                res
            
            if curSum > target:
                return
            
            for n in candidates:
                
                backtrack(curSum+n, curList + [n])
        
        backtrack(0, [])
        return res
                