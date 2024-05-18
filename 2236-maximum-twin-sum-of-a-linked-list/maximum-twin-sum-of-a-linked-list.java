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
    public int pairSum(ListNode head) 
    {
        int[] arrList = arrayTransfer(head);

        int front = 0;
        int rear = arrList.length - 1;
        int maxTwinSum = 0;
        int currentTwinSum = 0;

        while(rear > front)
        {
            currentTwinSum = arrList[front] + arrList[rear];

            if(currentTwinSum > maxTwinSum)
            {
                maxTwinSum = currentTwinSum;
            }

            front++;
            rear--;
        }

        return maxTwinSum;
    }

    public int[] arrayTransfer(ListNode head)
    {
        ListNode cursor = head;
        int length = 0;

        while (cursor != null)
        {
            cursor = cursor.next;
            length++;
        }

        int[] transferredArray = new int[length];
        cursor = head;

        for(int i = 0; i < length; i++)
        {
            transferredArray[i] = cursor.val;
            cursor = cursor.next;
        }

        return transferredArray;
    }
}