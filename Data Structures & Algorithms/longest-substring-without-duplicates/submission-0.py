class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        char_idx = {}

        for r in range(len(s)):
            char = s[r]

            if char in char_idx and char_idx[char] >= l:
                l = char_idx[char] + 1
            
            char_idx[char] = r

            res = max(r-l+1, res)
        
        return res