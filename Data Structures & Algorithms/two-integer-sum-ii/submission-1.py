class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        m = {} # dictionary to store the key:value pair of number:index(1 -indexed)
        for i,x in enumerate(numbers):
            y = target - x
            if y in m:
                return [m[y],i+1]
            m[x] = i+1