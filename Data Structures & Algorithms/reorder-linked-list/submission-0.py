# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Alternate between current list ordering and reversed ordering
        # Iterate pointer to center of list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Copy second half and reverse it
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Now iterate through existing list and update pointers
        dummy = ListNode(next=head)
        first, second = head, prev
        while second:
            flink, slink = first.next, second.next
            first.next = second
            second.next = flink
            first, second = flink, slink