class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols=len(matrix), len(matrix[0])
        low, high= 0, rows*cols-1
        while low<=high:
            mid = (low+high)//2
            mat=matrix[mid//cols][mid%cols]                   #[for rows][for columns]
            if  mat==target:               
                return True
            elif mat < target:
                low+=1
            else:
                high-=1
        return False