class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(set(nums)) < len(nums):
        #     return True
        # return False

        # Using HashMap
        seen = {}
        for n in nums:
            if n in seen and seen[n] >= 1:
                return True
            seen[n] = seen.get(n,0) + 1
        return False