class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return
        
        if m==0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        #opitmized
        i,j=0,0
        while i<m+n and j<n:
            if nums1[i] <= nums2[j] and i<m+j:
                i+=1
            elif j<n:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j+=1
                i+=1

        