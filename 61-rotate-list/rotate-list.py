# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        length = 0
        newK = 0

        curr = head
        while curr:
            length = length + 1
            curr = curr.next

        newK = k % length

        if newK == 0 or newK == length:
            return head

        curr = head
        for _ in range(length - newK - 1):
            curr = curr.next

        splitHead = curr.next
        curr.next = None

        curr = splitHead
        while curr.next:
            curr = curr.next

        curr.next = head

        return splitHead