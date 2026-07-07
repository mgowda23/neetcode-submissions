class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)-1):
        #     for j in range(len(nums)):
        #         if (nums[i]==nums[j] and i!=j):
        #             return True
        # return False
        return len(set(nums)) < len(nums)