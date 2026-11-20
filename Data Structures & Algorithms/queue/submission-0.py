class LinkNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        # Dummy Nodes
        self.head = LinkNode(-1)
        self.tail = LinkNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        new_val, prev, next = LinkNode(value), self.tail.prev, self.tail
        prev.next = new_val
        next.prev = new_val
        new_val.next = next
        new_val.prev = prev
        self.size += 1

    def appendleft(self, value: int) -> None:
        new_val, prev, next = LinkNode(value), self.head, self.head.next 
        prev.next = new_val
        next.prev = new_val
        new_val.next = next
        new_val.prev = prev
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        to_remove, prev, next = self.tail.prev, self.tail.prev.prev, self.tail  
        prev.next = next
        next.prev = prev
        self.size -= 1
        return to_remove.val
        

    def popleft(self) -> int:
        if self.size == 0:
            return -1
        to_remove, prev, next = self.head.next, self.head, self.head.next.next  
        prev.next = next
        next.prev = prev
        self.size -= 1
        return to_remove.val
        
