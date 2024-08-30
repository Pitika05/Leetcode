class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lSum=0
        rSum=sum(nums)
        ans=[]
        for i in nums:
            lSum+=i
            ans.append(abs(lSum-rSum))
            rSum-=i
        return ans