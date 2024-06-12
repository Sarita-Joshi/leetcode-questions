class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return nums
        if len(nums) == 1:
            return [str(nums[0])]
        
        res = []
        start, end = 0, 0
        while end < len(nums):
            while end+1 < len(nums) and nums[end+1] == nums[end] + 1:
                end += 1
            if end-start == 0:
                res.append(str(nums[end]))
            else:
                res.append(f"{nums[start]}->{nums[end]}")
            start, end = end+1, end+1
            
        return res
            
            
                    
                    
                
            
            