class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        r = nums1 + nums2
        r.sort()
        n = len(r)
        if n%2==0:
            med = n//2
            med = (r[med] + r[med-1]) / 2
        else:
            med = r[n//2]
        return med
            
        