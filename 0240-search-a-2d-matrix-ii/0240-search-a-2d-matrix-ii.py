class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols=len(matrix), len(matrix[0])
        low, high=0, cols-1
        while low<rows and high>=0:
            if matrix[low][high]==target:
                return True
            elif matrix[low][high]<target:
                low+=1
            else:
                high-=1
        return False
