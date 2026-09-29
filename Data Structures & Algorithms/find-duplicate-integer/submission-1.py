class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=0
        for i in range(len(nums)):
            if nums[n] ==-1:
                return n
            temp = nums[n]
            nums[n] = -1
            n = temp
        
        return n
            
            