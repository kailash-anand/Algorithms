class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:
    def __init__(self, homepage: str):
        self.history_list = ListNode(homepage)
        self.current = self.history_list

    def visit(self, url: str) -> None:
        new = ListNode(url)
        self.current.next = new
        new.prev = self.current
        self.current = self.current.next

    def back(self, steps: int) -> str:
        count = 0

        while self.current.prev and count < steps:
            self.current = self.current.prev
            count += 1
        
        return self.current.val

    def forward(self, steps: int) -> str:
        count = 0

        while self.current.next and count < steps:
            self.current = self.current.next
            count += 1
        
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)