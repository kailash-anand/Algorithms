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
class Solution 
{
    public ListNode deleteDuplicates(ListNode head) 
    {
        ListNode cursor = head;

        if(cursor == null || cursor.next == null)
        {
            return cursor;
        }

        while(cursor != null)
        {
            int currVal = cursor.val;

            while(cursor.next != null && cursor.next.val == currVal)
            {
                cursor.next = cursor.next.next;
            }

            cursor = cursor.next;
        }

        return head;
    }
}