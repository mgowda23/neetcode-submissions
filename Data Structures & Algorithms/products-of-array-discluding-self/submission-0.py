class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            if n!= 0:
                product = product * n
        
        res = []
        count_zeros = nums.count(0)
        for n in nums:
            if count_zeros >1:
                res.append(0)
            elif count_zeros == 1:
                if n == 0:
                    res.append(int(product))
                else:
                    res.append(0)
            else:
                res.append(product // n)
        return res