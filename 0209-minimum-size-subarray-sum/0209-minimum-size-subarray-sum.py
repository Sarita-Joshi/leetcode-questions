class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums[0]>=target:
            return 1
        if sum(nums)<target:
            return 0
        
        l=0
        r=0
        minlen = len(nums)
        sums = nums[l]
        
        while l < len(nums):
            if sums >= target:
                minlen = min(minlen, r-l+1)
                sums -= nums[l]
                l+=1
            elif r+1 < len(nums):
                r+=1
                sums += nums[r]
            else:
                break
        
        return minlen
               
            
            
            
                
            
            
    