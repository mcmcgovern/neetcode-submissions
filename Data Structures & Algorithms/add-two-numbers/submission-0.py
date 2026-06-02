# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum_list = []

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            current_sum = v1 + v2 + carry

            carry = current_sum // 10
            digit = current_sum % 10
            sum_list.append(digit)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result, link = None, None
        for i in range(len(sum_list)-1, -1, -1):
            result = ListNode(sum_list[i], link)
            link = result

        return result
        