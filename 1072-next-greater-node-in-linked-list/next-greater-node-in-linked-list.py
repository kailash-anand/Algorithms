# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Stack:
    def __init__(self):
        self.arr = []
        self.length = 0

    def push(self, val):
        self.arr.append(val)
        self.length += 1

    def pop(self):
        val = self.arr.pop(self.length - 1)
        self.length -= 1
        return val
    
    def peek(self):
        return self.arr[self.length - 1]

    def is_empty(self):
        return self.length == 0
        
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        answer = []
        node_arr = []
        stack = Stack()

        current = head
        while current:
            node_arr.append(current.val)
            answer.append(0)
            current = current.next

        for i in range(len(node_arr) - 1):
            stack.push(i)

            if node_arr[i + 1] > node_arr[i]:
                while not stack.is_empty() and node_arr[stack.peek()] < node_arr[i + 1]:
                    answer[stack.pop()] = node_arr[i + 1]

        return answer
            
        
