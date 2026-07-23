class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if not stack:
                    return False

                token = stack.pop()
                if char == ')' and token !='(':
                    return False
                if char == ']' and token !='[':
                    return False
                if char == '}' and token !='{':
                    return False
        return len(stack) == 0