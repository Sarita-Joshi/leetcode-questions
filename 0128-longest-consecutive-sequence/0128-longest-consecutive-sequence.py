class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        
        nums = sorted(nums)
        m = {}
        
        for i in range(len(nums)):
            if nums[i]-1 in m:
                
                m[nums[i]] = m[nums[i]-1] if m[nums[i]-1]!=None else nums[i]-1
            else:
                m[nums[i]] = None
        print(m)
        max = 0
        for k,v in m.items():
            if v!=None and k-v > max:
                max=k-v
        
        return max+1