class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        l = len(nums)-1
        for i in range(l,-1,-1):
            # print(nums, "i", i , "nums[i]", nums[i], "count", count)
            if nums[i]==val:
                nums[i] = nums[l-count]
                count += 1
        
        return l-count+1
                
            
        