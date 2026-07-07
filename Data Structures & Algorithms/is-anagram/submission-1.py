class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # count = Counter(s)
        # for c in t :
        #     count[c] -= 1
        #     if count[c] < 0 :
        #         return False
        # return True
        
        # ---------------------------
        map_s = defaultdict(int)
        map_t = defaultdict(int)
        
        for char in s: 
            map_s[char] += 1
        for char in t: 
            map_t[char] += 1
        
        if map_s == map_t: 
            return True
        else: 
            return False 

