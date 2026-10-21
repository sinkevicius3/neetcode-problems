class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        result = 0
        while (left < right):
            if max_left < max_right:
                left += 1
                if height[left] > max_left:
                    max_left = height[left]
                result += max_left - height[left]
            else:
                right -= 1
                if height[right] > max_right:
                    max_right = height[right]
                result += max_right - height[right]
        return result

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         max_left = [0] * n
#         max_right = [0] * n
#         for i in range(1, n):
#             if height[i - 1] > max_left[i - 1]:
#                 max_left[i] = height[i - 1]
#             else:
#                 max_left[i] = max_left[i - 1]

#             if height[n - i] > max_right[n - i]:
#                 max_right[n - 1 - i] = height[n - i]  
#             else:
#                 max_right[n - 1 - i] = max_right[n - i]

#         result = 0
#         for i in range(n):
#             water = min(max_left[i], max_right[i]) - height[i]
#             if water > 0:
#                 result += water

#         return result