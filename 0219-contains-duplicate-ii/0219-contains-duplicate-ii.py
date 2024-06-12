class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums)==1 or k==0:
            return False
        
        m = {}
        
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = i
                
            else:
                if abs(m[nums[i]] - i) <= k:
                    return True
                m[nums[i]]=i
        
        return False
            



            

