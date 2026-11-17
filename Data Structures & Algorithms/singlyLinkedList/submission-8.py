class LinkNode:
    def __init__(self, val, next = None):
        self.val = val 
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = self.tail = LinkNode(-1)
    
    # O(n)
    # Get i-th Node. Return -1 if out of bounds
    def get(self, index: int) -> int:
        idx = 0
        curr = self.head.next
        while curr:
            if idx == index:
                return curr.val
            curr = curr.next
            idx +=1 
        return -1
        
    # O(1)
    # Insert at front of list
    def insertHead(self, val: int) -> None:
        new_node = LinkNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        # set tail if it did not exist previously
        if not new_node.next:
            self.tail = new_node
        
    # O(1)
    # Insert at end of list
    def insertTail(self, val: int) -> None:
        new_node = LinkNode(val)
        self.tail.next = new_node
        self.tail = self.tail.next
        
    # O(n)
    # Remove i-th node. True if in-bounds. False if not.
    def remove(self, index: int) -> bool:
        idx = 0
        curr = self.head

        # navigate to index - 1
        while idx < index and curr:
            curr = curr.next
            idx += 1

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False
        
    # O(n)
    # Return list of all values
    def getValues(self) -> List[int]:
        values = []
        curr = self.head.next
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values