class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            n = len(stack) - 1
            if c == "+":
                stack[n - 1] += stack[n]
                stack.pop()
            elif c == "-":
                stack[n - 1] -= stack[n]
                stack.pop()
            elif c == "*":
                stack[n - 1] *= stack[n]
                stack.pop()
            elif c == "/":
                stack[n - 1] =  int(stack[n - 1] \
                    / stack[n])
                stack.pop()
            else:
                stack.append(int(c))
        return stack[0]