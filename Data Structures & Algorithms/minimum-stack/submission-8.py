class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # pushes val onto the end of the stack
    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)
        
    # removes the element at the end
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    # returns the element at the end
    def top(self) -> int:
        return self.stack[-1]

    # gets minimum value
    def getMin(self) -> int:
        return self.min_stack[-1]
