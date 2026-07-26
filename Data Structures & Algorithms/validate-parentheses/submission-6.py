class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ('{', '[', '('):
                stack.append(char)
            else:
                if not stack:
                    return False
                stack_top = stack.pop()
                if ((char == '}' and stack_top != '{') or
                    (char == ']' and stack_top != '[') or
                    (char == ')' and stack_top != '(')):
                    return False
        return len(stack) == 0