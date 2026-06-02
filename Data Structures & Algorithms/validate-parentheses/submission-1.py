class Solution:
    def isValid(self, s: str) -> bool:
        unresolved = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                unresolved.append(char)
            elif char == ')':
                if unresolved and unresolved[-1] == '(':
                    unresolved.pop()
                else:
                    return False
            elif char == ']':
                if unresolved and unresolved[-1] == '[':
                    unresolved.pop()
                else:
                    return False
            elif char == '}':
                if unresolved and unresolved[-1] == '{':
                    unresolved.pop()
                else:
                    return False
        return len(unresolved) == 0