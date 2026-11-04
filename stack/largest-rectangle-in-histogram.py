class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                p_index, p_height = stack.pop()
                max_area = max(max_area, p_height * (i - p_index))
                start = p_index
            stack.append((start, heights[i]))

        for i in range(len(stack)):
            max_area = max(max_area, stack[i][1] * (len(heights) - stack[i][0]))

        return max_area