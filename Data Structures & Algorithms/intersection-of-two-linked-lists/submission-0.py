# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # cycle detection + create loop
        loops = 15
        nodeA, nodeB = headA, headB
        while nodeA and nodeB and loops > 0:
            if nodeA == nodeB:
                return nodeA
            if nodeA.next == None:
                nodeA = headA
                loops -= 1
            else:
                nodeA = nodeA.next
            if nodeB.next == None:
                nodeB = headB
            else:
                nodeB = nodeB.next

        return None