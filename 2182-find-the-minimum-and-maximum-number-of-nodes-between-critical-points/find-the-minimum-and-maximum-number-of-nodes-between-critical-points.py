# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        node_arr = []
        critical_points = []
        result = [-1, -1]

        current = head
        while current:
            node_arr.append(current.val)
            current = current.next

        for i in range(1, len(node_arr) - 1):
            if node_arr[i] < node_arr[i - 1] and node_arr[i] < node_arr[i + 1]:
                critical_points.append(i)
            elif node_arr[i] > node_arr[i - 1] and node_arr[i] > node_arr[i + 1]:
                critical_points.append(i)

        if len(critical_points) > 1:
            min = critical_points[1] - critical_points[0]
            for i in range(len(critical_points) - 1):
                if critical_points[i + 1] - critical_points[i] < min:
                    min = critical_points[i + 1] - critical_points[i]

            max = critical_points[len(critical_points) - 1] - critical_points[0]

            result[0] = min
            result[1] = max

        return result

