/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} head
     * @return {ListNode}
     */
    reverseList(head) {

        let prev = null;
        let cursor = head;

        while (cursor) {
            let nextTemp = cursor.next; // save next
            cursor.next = prev;         // reverse pointer
            prev = cursor;              // move prev forward
            cursor = nextTemp;          // move curr forward
        }

        return prev; // new head
    }
}
