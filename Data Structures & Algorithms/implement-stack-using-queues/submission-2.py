# One Queue Version

class MyStack:

    def __init__(self):
        self.queue = deque()
        
    # Pushes element to top of the stack
    def push(self, x: int) -> None:
        # push element to back of the queue
        self.queue.append(x)
        last_idx = len(self.queue) - 1
        count = 0

        # while count < idx of last el
        while count < last_idx:
        #   popleft
            val = self.queue.popleft()
        #   append el to back of queue
            self.queue.append(val)
            count += 1 
        
    # Removes the element on the top of the stack
    def pop(self) -> int:
        return self.queue.popleft()
        
    # Returns the element on the top of the stack
    def top(self) -> int:
        if self.empty():
            return None

        return self.queue[0]
        
    # Returns true if stack is empty, false otherwise
    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()