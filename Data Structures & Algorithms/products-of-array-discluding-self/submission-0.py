class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Prefix Product and Suffix Product 
        suffix, prefix = 1, 1

        n = len(nums)
        res = [1] * n

        #Prefix product or left product:
        for i in range(n):
           res[i] = prefix
           prefix *= nums[i]

        #Suffix product or right product:
        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
    
        return res