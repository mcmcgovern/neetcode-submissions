# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr = ListNode(next=head)
        while curr:
            skip = m
            while curr and skip:
                curr = curr.next
                skip -= 1
            
            remove = n
            while curr and curr.next and remove:
                curr.next = curr.next.next
                remove -= 1

        return head