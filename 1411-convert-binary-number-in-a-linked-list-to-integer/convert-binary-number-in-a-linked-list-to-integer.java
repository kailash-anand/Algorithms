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
    public int getDecimalValue(ListNode head) 
    {
        ListNode cursor = head;
        int length = 0;
        int number = 0;

        while(cursor != null)
        {
            length++;
            cursor = cursor.next;
        }

        cursor = head;
        length--;

        while(cursor != null)
        {
            if(cursor.val == 1)
            {
                number += Math.pow(2, length);
            }

            length--;
            cursor = cursor.next;
        }

        return number;
    }
}