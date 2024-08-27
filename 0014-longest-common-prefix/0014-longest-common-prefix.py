class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=strs[0]
        pref_len=len(pref)

        for s in strs[1:]:
            while pref != s[0:pref_len]:
                pref_len -= 1
                pref = pref[0:pref_len]

                if pref_len == 0:
                    return ""
        return pref