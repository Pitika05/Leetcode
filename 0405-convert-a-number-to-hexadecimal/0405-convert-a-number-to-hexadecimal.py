class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        
        hex_digits = "0123456789abcdef"
        hex_result=[]

        if num < 0:
            num += 2 ** 32  

        while num>0:
            remainder = num%16
            hex_result.append(hex_digits[remainder])
            num//=16
        
        return ''.join(hex_result[::-1])
        