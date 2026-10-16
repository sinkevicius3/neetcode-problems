class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for current in range(len(nums) - 2):
            if current > 0 and nums[current] == nums[current - 1]:
                continue
            target = -nums[current]
            left = current + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.append([nums[current], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right + 1]):
                        right -= 1
                    
        return result