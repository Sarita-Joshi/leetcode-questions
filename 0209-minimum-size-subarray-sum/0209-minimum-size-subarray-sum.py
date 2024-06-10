class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        
        l=0
        r=0
        minlen = len(nums)
        sums = 0
        
        for r in range(len(nums)):
            sums += nums[r]
            
            while sums >= target:
                minlen = min(minlen, r-l+1)
                sums -= nums[l]
                l+=1
                

        return minlen
               
            
            
            
                
            
            
    