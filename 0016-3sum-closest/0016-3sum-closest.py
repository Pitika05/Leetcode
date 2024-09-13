class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        resultSum=nums[0]+nums[1]+nums[2]
        minDiff=float('inf')

        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == target:
                    return target
                elif sum < target:
                    left+=1
                else:
                    right-=1

                diff = abs(sum-target)

                if diff < minDiff:
                    resultSum = sum
                    minDiff = diff

        return resultSum