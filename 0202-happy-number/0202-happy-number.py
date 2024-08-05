class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            num=n
            total=0
            while num>0:
                digit=num%10
                total+=digit**2
                num=num//10
            return total
        
        for i in range(100):
            n= sumOfSquares(n)
            if n==1:
                return True
        else:
            return False
