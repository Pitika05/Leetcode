class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        
        pre1=1
        pre2=0
        for i in range(2,n+1):
            curr=pre1+pre2
            pre2=pre1
            pre1=curr
        return pre1