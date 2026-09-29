class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [0,1]
        mp = {}
        for i,n in enumerate(nums):
            if n in mp and i!= mp[n]:
                return [mp[n],i]
            mp[target-n] = i