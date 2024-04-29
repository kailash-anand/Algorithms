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
    public ListNode oddEvenList(ListNode head) {
        ListNode firstHalf = null;
        ListNode secondHalf = null;
        int indexCount = 1;

        ListNode cursor = head;
        ListNode secondHalfHead = secondHalf;
        ListNode firstHalfHead = firstHalf;


        if(head == null)
        {
            return head;
        }

        while(cursor != null)
        {
            if(isEven(indexCount))
            {
                if(secondHalf == null)
                {
                    secondHalf = new ListNode(cursor.val);
                    secondHalfHead = secondHalf;
                }
                else
                {
                    ListNode temp = new ListNode(cursor.val);
                    secondHalf.next = temp;
                    secondHalf = secondHalf.next;
                }
            }
            else
            {
                if(firstHalf == null)
                {
                    firstHalf = new ListNode(cursor.val);
                    firstHalfHead = firstHalf;
                }
                else
                {
                    ListNode temp = new ListNode(cursor.val);
                    firstHalf.next = temp;
                    firstHalf = firstHalf.next;
                }
            }

            cursor = cursor.next;
            indexCount++;
        }

        firstHalf.next = secondHalfHead;

        return firstHalfHead;
    }

    public boolean isEven(int number)
    {
        return (number % 2) == 0;
    }
}