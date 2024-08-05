
class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        s = set()  # Set to keep track of numbers we have encountered
        while  n != 1 and n not in s:
            s.add(n)  # Add the current number to the set
            n = sumOfSquares(n)  # Compute the next number in the sequence
            
        return n==1
        