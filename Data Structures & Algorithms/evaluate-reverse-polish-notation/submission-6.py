class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                term2 = stack.pop()
                term1 = stack.pop()
                if token == '+':
                    stack.append(term1+term2)
                if token == '-':
                    stack.append(term1-term2)
                if token == '*':
                    stack.append(term1*term2)
                if token == '/':
                    stack.append(int(term1/term2))
        return stack.pop()