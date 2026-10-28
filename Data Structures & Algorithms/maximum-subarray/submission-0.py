class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm:
        currsum = 0
        maxsum = nums[0]

        for n in nums:
            currsum += n
            maxsum = max(maxsum, currsum)

            if currsum < 0:
                currsum = 0
        return maxsum