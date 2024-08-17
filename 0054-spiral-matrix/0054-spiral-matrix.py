class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        top, left = 0, 0
        bottom, right = rows - 1, cols - 1
        direction = 0
        result = []

        while top <= bottom and left <=right:
            #dir=0 top to right
            if direction == 0: 
                for i in range(top, right+1):
                    result.append(matrix[top][i])
                top += 1 
            #dir=1 top to bottom
            elif direction == 1: 
                for i in range(top, bottom+1):
                    result.append(matrix[i][right])
                right -= 1
            #dir=2 right to left
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            #dir=3 bottom to top
            elif direction == 3:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1 
            
            direction = (direction + 1) % 4
        return result