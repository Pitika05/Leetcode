class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        sorted_str1=sorted(s)
        sorted_str2=sorted(t)
        return True if sorted_str1==sorted_str2 else False