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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size =0;
        if(head == null){
            return null;
        }
        ListNode curr = head;
        while(curr != null){
            size++;
            curr = curr.next;
        }
        if(size == n){
            return head.next;
        }
        ListNode temp = head;
        for(int i=0; i<size-n-1; i++){
            temp = temp.next;
        }
        temp.next = temp.next.next;
        return head;
        
    }
}