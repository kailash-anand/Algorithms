# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        left = head
        right = head.next
        head = head.next

        while True:
            left.next = right.next
            right.next = left

            left = right
            right = right.next

            if right.next != None and right.next.next != None:
                temp = right
                right = right.next
                left = right
                right = right.next
                temp.next = temp.next.next
            else:
                break

        return head
