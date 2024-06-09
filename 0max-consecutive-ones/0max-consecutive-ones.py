class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count=0
        maxw=0

        for i in nums:
            if i==1:
                count+=1
            elif i==0:
                if count > maxw:
                    maxw = count
                count=0
        return max(maxw,count)
                
                