class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        maxl = 0
        l = 0
        nums = sorted(nums)

        for i in range(1, len(nums)):
            print(i, nums[i],nums[i-1], l, maxl)
            if nums[i] == nums[i-1]+1:
                l+=1
            elif nums[i] != nums[i-1]:
                maxl = max(maxl,l)
                l=0  
        return max(maxl, l)+1  
            
