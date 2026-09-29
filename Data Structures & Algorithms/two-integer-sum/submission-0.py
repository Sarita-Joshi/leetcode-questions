class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==2:
            return [0,1]

        comp = {}
        
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in comp:
                return [comp[temp], i]
            comp[nums[i]] = i 