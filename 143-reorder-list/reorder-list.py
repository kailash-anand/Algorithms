# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        start = head
        end = head
        length = 0

        while end != None:
            length += 1
            end = end.next

        middle = length // 2

        for i in range(middle):
            start = start.next

        prev = start
        left = start.next
        right = left.next if left is not None else None

        prev.next = None
        while left is not None:
            left.next = prev

            prev = left
            left = right
            right = right.next if right is not None else None

        startLeft = head
        startRight = head.next
        endRight = prev
        endLeft = prev.next

        while startRight is not None and endLeft is not None:
            startLeft.next = endRight
            startLeft = startRight
            startRight = startRight.next

            endRight.next = startLeft
            endRight = endLeft
            endLeft = endLeft.next