# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Approaches:
#   A. Recursively - O(n) time, O(n) space
#       Base case: 
#           if not head.next:
#               return head
#       Body:
#           
#   B. Iteratively - O(n) time, O(1) space <- ideal
#       

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        # 1. initialize `prev` at head, and `next` at head.next
        prev, next = None, head

        # 2. while curr exists
        #   - capture next2
        #   - point next.next to prev
        #   - set prev to next
        #   - set curr to next2
        while next:
            next2 = next.next
            next.next = prev
            prev = next
            next = next2
        
        # 3. return prev (new head)
        return prev