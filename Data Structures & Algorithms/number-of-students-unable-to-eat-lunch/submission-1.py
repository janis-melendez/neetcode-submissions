# Approach A: Simulate (Use Queue)
# O(n^2) Time and O(n) space
# - create student queue
# - loop while progress is being made
# - compare front student to top sandwich
# - rotate or pop

# Approach B: counting
# O(n) time and O(1) space
# - count how many students prefer each type
# - walk sandwiches: if count > 0, consume; else break
# - return leftover students 

class LinkNode:
    def __init__(self, val = -1):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self, array: List[int]):
        self.head = LinkNode(-1)
        self.tail = LinkNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0
        for el in array:
            self.insert_tail(el)

    def get_front(self) -> Optional[int]:
        if self.head.next != self.tail:
            return self.head.next.val
        return None

    # Insert node at back of list
    def insert_tail(self, val) -> None:
        new_node, prev, next = LinkNode(val), self.tail.prev, self.tail 

        # 1. update surrounding nodes
        prev.next = new_node
        next.prev = new_node

        # 2. point value to surrounding nodes
        new_node.prev = prev
        new_node.next = next
        self.length += 1

    # Remove from front of array
    def pop_left(self) -> Optional[int]:
        if self.head.next == self.tail:
            return None
        
        # 1. find target, prev (dummy) and next_after
        target, prev, next_after = self.head.next, self.head, self.head.next.next
        # 2. capture target value
        value = target.val
        
        # 3. if target is not the tail: 
        prev.next = next_after
        next_after.prev = prev
        self.length -= 1
        return value

    def get_length(self) -> int:
        return self.length

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        queue = Deque(students)
        rotations = 0
        idx = 0

        #  2. while queue is not empty and rotations less than number of students
        while queue.get_length() > 0 and rotations < queue.get_length():
            front = queue.get_front()
            if front == sandwiches[idx]:
                idx += 1
                queue.pop_left()
                rotations = 0
            else:
                student = queue.pop_left()
                queue.insert_tail(student)
                rotations += 1

        #  3. return n
        return queue.get_length()