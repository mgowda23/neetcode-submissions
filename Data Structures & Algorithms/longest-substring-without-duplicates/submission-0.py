class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l, max_len = 0, 0

        for r in range(len(s)):
            ch = s[r]

            if ch in mp:
                l = max(l,mp[ch]+1)
            
            mp[ch] = r
            max_len = max(max_len, r-l+1)
       
        return max_len