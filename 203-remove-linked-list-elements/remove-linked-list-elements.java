/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) 
    {
        if(head == null)
        {
            return head;
        }

        ListNode cursor = head;

        while((head != null) && (head.val == val))
        {
            head = head.next;
        }

        cursor = head;

        while((cursor != null) && (cursor.next != null))
        {
            if(cursor.next.val == val)
            {
                cursor.next = cursor.next.next;
                continue;
            }

            cursor = cursor.next;
        }

        return head;    
    }
}