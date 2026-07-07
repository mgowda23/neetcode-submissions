class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {}
        for i, x in enumerate(numbers):
            y = target - x
            if y in m:
                return [m[y],i+1]
            m[x] = i+1
        