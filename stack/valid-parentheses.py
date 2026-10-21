class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1:
            return False
        stack = []
        hashmap = {")": "(", "}": "{", "]": "["} 
        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack

# also correct

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for c in s:
#             if c == "(" or c == "{" or c == "[":
#                 stack.append(c)
#             else:
#                 if not stack:
#                     return False
#                 popped = stack.pop() 
#                 if (c == ")" and popped != "(") or \
#                     (c == "}" and popped !=  "{") or \
#                     (c == "]" and popped != "["):
#                     return False
#         return not stack