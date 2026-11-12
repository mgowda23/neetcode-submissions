class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        for c in t:freq[c] = freq.get(c,0) + 1

        l, count = 0, len(t)
        min_len = float('inf')
        ans = ""

        # Expanding to find the valid substring:
        for r in range(len(s)):
            ch = s[r]

            if ch in freq:
                if freq[ch] > 0:
                    count -= 1
                freq[ch] -= 1

        # Shrinking to find the smallest substring:
            while count == 0:
                if (r-l+1) < min_len:
                    min_len = r-l+1
                    ans = s[l:r+1]
                
                lch = s[l]
        
                if lch in freq:
                    freq[lch] += 1
                    if freq[lch] > 0:
                        count += 1
                l+=1

        return ans