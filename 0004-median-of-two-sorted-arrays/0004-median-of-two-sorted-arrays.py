class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = nums1 + nums2      
        old = sorted(new)
        n = len(old)
        if n%2!=0:
            return old[n//2]
        else:
            mid1 = old[n//2 - 1]
            mid2 = old[n//2]
            return (mid1 + mid2)/2