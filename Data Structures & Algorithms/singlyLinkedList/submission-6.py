class LinkNode:
    def __init__(self, val, next_node = None):
        self.val = val
        self.next = next_node

class LinkedList:  
    def __init__(self):
        # Dummy node
        self.head = LinkNode(-1)
        self.tail = self.head

    # Returns i-th node. Returns -1 if out of bounds
    def get(self, index: int) -> int:
        curr = self.head.next
        idx = 0
        while curr:
            if idx == index:
                return curr.val
            curr = curr.next
            idx += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = LinkNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = LinkNode(val)
        # point tail to new node and update tail
        self.tail.next = new_node
        self.tail = self.tail.next        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        # navigate to index - 1
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False 
        

    def getValues(self) -> List[int]:
        values_list = []
        curr = self.head.next
        while curr:
            values_list.append(curr.val)
            curr = curr.next
        return values_list

