class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1=len(nums1)
        n2=len(nums2)
        total=n1+n2

        merge=nums1+nums2
        merge.sort()

        if total%2==0:
            median=(merge[total//2 -1]+merge[total//2]) / 2
        else:
            median=merge[total//2]
       
        return median