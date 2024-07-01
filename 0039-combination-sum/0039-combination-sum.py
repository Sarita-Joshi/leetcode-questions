class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()
        def backtrack(i, curSum, curList):
            if curSum == target:
                res.add(tuple(curList))
                res
            
            if curSum > target:
                return
            
            for j, n in enumerate(candidates):
                if j >= i:
                    backtrack(j, curSum+n, curList + [n])
        
        backtrack(0, 0, [])
        return res
                