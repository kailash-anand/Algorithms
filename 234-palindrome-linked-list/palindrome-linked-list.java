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
    public boolean isPalindrome(ListNode head) {
         Deque<Integer> intStack = new ArrayDeque<Integer>();
        boolean check = false; 

        ListNode cursor = head;
    
        while(cursor != null)
        {
            intStack.push(cursor.val);
            cursor = cursor.next;
        }

        cursor = head;

        while(cursor != null)
        {
            if(cursor.val != intStack.pop())
            { return false;}

            cursor = cursor.next;
        }

        return true;
    }
}