class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif char == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif char == '}':
                if not stack or stack.pop() != '{':
                    return False
            else:
                return False
        return len(stack) == 0