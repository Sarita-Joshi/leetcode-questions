class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r) //2
            print(mid, [l,r], nums[l:r+1])
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[mid] < target or nums[l] > target:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid-1
                else:
                    l = mid+1

        return -1
