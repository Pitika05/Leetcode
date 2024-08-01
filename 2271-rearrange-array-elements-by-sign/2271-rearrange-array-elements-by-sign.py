class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives=[]
        negatives=[]

        for num in nums:
            if num>0:
                positives.append(num)
            else:
                negatives.append(num)
        
        arr=[0]*len(nums)
        k=0

        for pos,neg in zip(positives,negatives):
            arr[k]=pos
            arr[k+1]=neg
            k+=2
        return arr