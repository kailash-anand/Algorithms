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
        # Find length
        start = head
        end = head
        length = 0

        while end != None:
            length += 1
            end = end.next

        # Get middle 
        middle = length // 2

        # Go to middle
        for i in range(middle):
            start = start.next

        prev = start
        left = start.next
        right = left.next if left is not None else None

        # Reverse list only from middle. Also remove cyclic pointer at middle
        # Essentially, middle pointer has no next for now
        # 1 -> 2 -> 3 <- 4 <- 5 (In this format)
        prev.next = None
        while left is not None:
            left.next = prev

            prev = left
            left = right
            right = right.next if right is not None else None

        # Zig zag merge
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