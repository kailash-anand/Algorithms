/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) 
    {
        if((headA == null) || (headB == null))
        {
            return null;
        }

        if(headA == headB)
        {
            return headA;
        }

        int lengthofA = getLength(headA);
        int lengthofB = getLength(headB);
        int diff = 0;
        char greater = '-';
        ListNode cursorA = headA;
        ListNode cursorB = headB;

        if(lengthofA > lengthofB)
        {
            diff = lengthofA - lengthofB;
            greater = 'A';
        }
        else
        {
            diff = lengthofB - lengthofA;
            greater = 'B';
        }

        if(greater == 'A')
        {
            for(int i = 0; i < diff; i++)
            {
                cursorA = cursorA.next;
            }
        }
        else
        {
            for(int i = 0; i < diff; i++)
            {
                cursorB = cursorB.next;
            }
        }

        if(cursorA == cursorB)
        {
            return cursorA;
        }

        while((cursorA != null) && (cursorB != null))
        {
            if((cursorA.next != null) && (cursorA.next == cursorB.next))
            {
                return cursorA.next;
            }

            cursorA = cursorA.next;
            cursorB = cursorB.next;
        }

        return null;
    }

    public int getLength(ListNode node)
    {
        int count = 0;

        while(node != null)
        {
            count++;
            node = node.next;
        }

        return count;
    }
}