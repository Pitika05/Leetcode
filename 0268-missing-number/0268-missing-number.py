class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=n*(n+1)//2
        sum=0
        for i in range(n):
            sum+=nums[i]    #array sum
        return total-sum

