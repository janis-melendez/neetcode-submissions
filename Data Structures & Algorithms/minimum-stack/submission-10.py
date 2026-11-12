# NOTE: Each function needs to run in O(1)
class MinStack:

    # Initialize stack and min stack
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    # Pushes element onto stack
    def push(self, val: int) -> None:
        self.stack.append(val)
        # compare val to last val of min stack, append min to min_stack
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    # Removes element of the top of the stack
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    # Gets top element of stack
    def top(self) -> int:
        return self.stack[-1]
        
    # return last value from min stack
    def getMin(self) -> int:
        return self.min_stack[-1]
        
