class LinkNode:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = LinkNode(homepage) 
        self.tail = self.head

        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.curr_page = self.head
        

    def visit(self, url: str) -> None:
        new_url = LinkNode(url)
        self.curr_page.next = new_url
        new_url.prev = self.curr_page
        self.curr_page = new_url
        self.tail = new_url

    def back(self, steps: int) -> str:
        curr = self.curr_page

        while steps > 0 and curr:
            steps -= 1
            curr = curr.prev

        if curr:
            self.curr_page = curr
            return curr.val

        # Return homepage by default
        self.curr_page = self.head
        return self.head.val

    def forward(self, steps: int) -> str:
        curr = self.curr_page

        while steps > 0 and curr:
            steps -= 1
            curr = curr.next
        
        if curr:
            self.curr_page = curr
            return curr.val
        
        # By default, return tail
        self.curr_page = self.tail
        return self.tail.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)