class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for elem in nums:
            if elem in result:
                return True
            result.add(elem)
        return False