# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 0:
            return []

        if len(lists) == 1:
            return lists[0]

        mergedList = self.mergeTwoLists(lists[0], lists[1])
        for i in range(2, len(lists)):
            mergedList = self.mergeTwoLists(mergedList, lists[i]) 

        return mergedList

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(-1)
            head = dummy

            while list1 and list2:
                if list1.val <= list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next

                head = head.next

            if list1:
                head.next = list1
            elif list2:
                head.next = list2

            return dummy.next

        