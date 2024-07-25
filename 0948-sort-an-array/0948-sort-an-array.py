class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        a=nums
        def merge(left,right):
            merg=[]
            i=0
            j=0

            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    merg.append(left[i])
                    i+=1
                else:
                    merg.append(right[j])
                    j+=1
            while i<len(left):
                merg.append(left[i])
                i+=1
            while j<len(right):
                merg.append(right[j])
                j+=1
            return merg

        def merge_sort(a):
            if len(a)==1:
                return a
            
            mid = int(len(a)/2)
            left=merge_sort(a[:mid])
            right=merge_sort(a[mid:])

            return merge(left,right)

        return merge_sort(a)
