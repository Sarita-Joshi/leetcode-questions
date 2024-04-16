class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        count=1
        for j in nums[1:]:
            if nums[i] != j:
                count=1 
            else:
                count+=1  

            if count <=2:
                    i= i+1
                    nums[i] = j

        return i+1