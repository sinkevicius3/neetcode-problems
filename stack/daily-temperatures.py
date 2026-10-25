class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                    popped_idx = stack.pop()
                    result[popped_idx] = i - popped_idx
            stack.append(i)
        return result