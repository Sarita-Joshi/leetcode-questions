class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2:
            return [0,1]
        
        hmap = {}

        for i,n in enumerate(nums):
            if target-n in hmap:
                return [hmap[target-n],i]
            hmap[n] = i
        
        return [-1,-1]