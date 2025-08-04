# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        head = list1 if list1.val < list2.val else list2
        result = head
        if head is list1:
            list1 = list1.next
        elif head is list2:
            list2 = list2.next

        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                head = head.next
                list1 = list1.next
            elif list2.val <= list1.val:
                head.next = list2
                head = head.next
                list2 = list2.next

        if list1:
            head.next = list1
        else:
            head.next = list2

        return result