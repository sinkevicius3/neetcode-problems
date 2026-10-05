class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            num_set.add(num)
        return len(num_set) != len(nums)