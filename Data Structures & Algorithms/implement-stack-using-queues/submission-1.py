# Constaints:
# Can only use operations of a base queue:
# - append
# - popleft
# DO NOT USE:
# - pop

# Queue = Remove from the front
# Stack = Remove from the back

# .push(1), .push(2), .push(3[]

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    # Pushes element to the top of the stack
    def push(self, x: int) -> None:
        # push el to q1
        self.q1.append(x)
        
    # Removes the element on the top of the stack
    def pop(self) -> int:
        last_idx = len(self.q1) - 1
        count = 0
        
        # push all elements from q1 to q2 (except 1)
        while count < last_idx:
            val = self.q1.popleft()
            self.q2.append(val) 
            count += 1
        
        # grab last element of q1
        res = self.q1.popleft()
        
        # swap q1 and q2
        temp_q1 = self.q1
        self.q1 = self.q2
        self.q2 = temp_q1

        return res

    # Returns the element on the top of the stack
    def top(self) -> int:
        if self.empty(): return None

        return self.q1[-1]
        
    # Returns true if stack is empty
    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()