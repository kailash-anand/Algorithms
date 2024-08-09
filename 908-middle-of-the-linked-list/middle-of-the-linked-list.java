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
    public ListNode middleNode(ListNode head) 
    {
        ListNode cursor = head;
        int length = 0;
        int mid = 0;

        while(cursor != null)
        {
            length++;
            cursor = cursor.next;
        }

        mid = length / 2;
        cursor = head;

        for(int i = 0; i < mid; i++)
        {
            cursor = cursor.next;
        }

        return cursor;
    }
}