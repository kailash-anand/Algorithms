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
    public ListNode deleteMiddle(ListNode head) {
        int size = getSize(head);
        int middle = size/2;
        int index = 0;
        ListNode temp = head;

        if(size == 1)
        {
            return null;
        }
        
        while(index < middle-1)
        {
            index++;
            temp = temp.next;
        }

        if(temp == null || temp.next == null)
        {
            return head;
        }

        temp.next = temp.next.next;

        return head;
    }

    public int getSize(ListNode head)
    {
        ListNode temp = head;
        int count = 0;

        while(temp != null)
        {
            count++;
            temp = temp.next;
        }

        return count;
    }
}