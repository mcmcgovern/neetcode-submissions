# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first calculate list length
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length == 1:
            return None

        index = length - n
        if index == 0:
            return head.next

        index -= 1
        node = head
        i = 0
        while node:
            print(i, index)
            if i == index:
                node.next = node.next.next
                break
            else:
                i += 1
                node = node.next
        return head