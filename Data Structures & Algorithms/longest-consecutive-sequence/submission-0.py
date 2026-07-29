class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # to remove duplicates
        ans = 0

        for n in nums:
            if n-1 not in num_set: # to check if it can be the start of sepquence
                curr = n
                count = 1

                while curr+1 in num_set:
                    curr += 1
                    count +=1
                ans = max(ans, count)
        
        return ans