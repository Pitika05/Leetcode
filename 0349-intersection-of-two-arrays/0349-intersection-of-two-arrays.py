class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for i in nums1:
            for j in nums2:
                if i==j and j not in result:
                    result.append(j)
        return result 