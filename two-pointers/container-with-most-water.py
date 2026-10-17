class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_amount = 0
        while left < right:
            amount = min(heights[left], heights[right]) * (right - left)
            if amount > max_amount:
                max_amount = amount
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_amount