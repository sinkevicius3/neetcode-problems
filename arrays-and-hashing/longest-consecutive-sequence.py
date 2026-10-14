class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_seq = 0
        for num in nums:
            if num - 1 not in numset:
                cur_seq = 1
                while num + cur_seq in numset:
                    cur_seq += 1
                if cur_seq > max_seq:
                    max_seq = cur_seq
        return max_seq