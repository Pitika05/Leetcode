class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum=0
        n=len(mat)
 
        #Get the sum of both diagonals
        for i in range(n):
            sum += mat[i][i]
            sum += mat[i][n-i-1]
        
        #If the matrix is odd subtract the duplicate element
        if n%2 != 0:
            sum -= mat[n//2][n//2]
        
        return sum
