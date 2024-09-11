class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row=False
        first_col=False

        #Set markers in first row and first column
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i==0:
                        first_row=True
                    if j==0:
                        first_col=True
                    matrix[0][j]=0
                    matrix[i][0]=0

        #Replace inner matrix
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        
        #Last remaining checks for the first row and first column
        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j]=0
        
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0]=0