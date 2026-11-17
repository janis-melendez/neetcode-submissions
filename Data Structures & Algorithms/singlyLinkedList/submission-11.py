class LinkNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        # Dummy. Makes removing head easier. 
        self.head = self.tail = LinkNode(-1)
    
    # Get i-th node. Returns -1 if out of bounds.
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        
        return -1

    # Insert node at beginning of list. O(1)
    def insertHead(self, val: int) -> None:
        new_node = LinkNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    # Insert node at the end of list. O(1) 
    def insertTail(self, val: int) -> None:
        new_node = LinkNode(val)
        self.tail.next = new_node
        self.tail = self.tail.next

    # Remote i-th node. Return False if out of bounds. O(n)
    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        # navigate to node before index
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False

    # Return list of all values. O(n)
    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next

        while curr:
            values.append(curr.val)
            curr = curr.next

        return values
        
