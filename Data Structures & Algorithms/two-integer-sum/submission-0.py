class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} #hashmap/dictionary to store the key value pairs
        for i,x in enumerate(nums):
            y = target - x
            if y in m:
                return [m[y], i]
            m[x] = i