/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) 
    {
        if(head == null || head.next == null)
        {
            return false;
        }

        ListNode slow = head;
        ListNode fast = head.next;

        while((fast != null) && (fast != slow))
        {
            fast = fast.next;

            if(fast == null || fast == slow)
            {
                break;
            }

            slow = slow.next;
            fast = fast.next;
        }

        if(fast == null)
        {
            return false;
        }
        else
        {
            return true;
        } 
    }
}