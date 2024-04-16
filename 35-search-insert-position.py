class Solution:

    def bsearch(self, arr, high, low, k):
        res = high
        if high>low:    
            mid = int((high + low)/2)
            
            if arr[mid] == k:
                return mid
            if k < arr[mid]:
                res = self.bsearch(arr, mid, low, k)
                if res==-1:
                    res= mid-1
            elif k > arr[mid]:
                res=self.bsearch(arr, high, mid+1, k)
                if res==-1:
                    res= mid+1
        return res


    def searchInsert(self, nums: List[int], target: int) -> int:

        return self.bsearch(nums, len(nums), 0, target)