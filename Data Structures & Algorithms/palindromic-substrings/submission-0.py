class Solution:
    def countSubstrings(self, s: str) -> int:
        # Expand from middle approach(as in considering each letter to be middle char and expanding both sides to check if its a palindrome)
        res = 0
        
        for i in range(len(s)):
            #odd length
            res += self.countPals(s, i, i)
            #even length
            res += self.countPals(s, i, i+1)

        return res
    
    def countPals(self, s, l, r):
        res = 0

        while l >= 0 and r < len(s) and s[l]==s[r]:
            res += 1
            l -= 1
            r += 1
        return res