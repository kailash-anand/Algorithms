# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None and n == 1:
            head = None
            return head

        list_length = 0

        current = head
        while current:
            list_length += 1
            current = current.next

        num_to_traverse = list_length - n - 1

        if num_to_traverse == -1:
            head = head.next
            return head

        current = head
        for i in range(num_to_traverse):
            current = current.next
        if current != None and current.next != None:
            current.next = current.next.next

        return head


        

    

    

        