class MinStack:

    def __init__(self):
        self.stack = [] # store pushed value with current min value

    def push(self, val: int) -> None:
        if not self.stack:
            # store val and current min, which is going to be val since it is the only value
            self.stack.append((val, val))
        else:
            prev_min = self.stack[-1][1]
            self.stack.append((val, min(prev_min, val)))

    def pop(self) -> None:
        if not self.stack:
            return None
        else:
            self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        
