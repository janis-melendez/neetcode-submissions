class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:   
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    # O(n). Get the value of the i-th node.
    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        
        curr_node = self.head
        idx = 0

        while curr_node != None:
            if idx == index:
                return curr_node.val
            idx += 1
            curr_node = curr_node.next
            
    # O(1). Insert node at the head of the list.
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        self.length += 1

        # if empty, set new head / tail
        if self.head is None:
            self.head = self.tail = new_node
            return

        # set new head
        new_node.next = self.head
        self.head = new_node
        
    # O(1). Insert node at the tail of the list
    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.length += 1

        # if empty, set new head and tail
        if self.head is None:
            self.head = self.tail = new_node
            return
        
        # insert node at end of list
        self.tail.next = new_node
        self.tail = new_node

    # O(n). Remove node at the i-th index
    def remove(self, index: int) -> bool:
        if index >= self.length:
            return False
            
        self.length -= 1

        if index == 0:
            self.head = self.head.next
            if self.length == 0:
                self.tail = None
            return True

        prev_node = None
        curr_node = self.head

        for _ in range(index):
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.next = curr_node.next

        if prev_node.next is None:
            self.tail = prev_node

        return True
        
    # O(n). Return an array of all values in the list, head to tail
    def getValues(self) -> List[int]:
        values = []
        curr_node = self.head

        while curr_node != None:
            values.append(curr_node.val)
            curr_node = curr_node.next

        return values