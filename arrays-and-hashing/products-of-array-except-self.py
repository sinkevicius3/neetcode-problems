class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [None] * n
        suffix = [None] * n
        output = [None] * n

        prefix[0] = nums[0]
        suffix[n - 1] = nums[n - 1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
            suffix[n - 1 - i] = suffix[n - i] * nums[n - 1 - i]

        output[0] = suffix[1]
        output[n - 1] = prefix[n - 2]
        for i in range(1, n - 1):
            output[i] = prefix[i - 1] * suffix[i + 1]

        return output