# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head.next

        while fast is not None and slow != fast:
            fast = fast.next.next if fast.next is not None else fast.next
            slow = slow.next

        if fast is None:
            return False
        else:
            return True