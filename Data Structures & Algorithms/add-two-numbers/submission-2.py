# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        curr = start

        carry_over = ListNode()

        node1 = l1
        node2 = l2

        while node1 != None or node2 != None or carry_over.val > 0:
            node_sum = 0
            node_sum += carry_over.val

            if node1:
                node_sum += node1.val
                node1 = node1.next

            if node2:
                node_sum += node2.val
                node2 = node2.next


            if node_sum >= 10:
                carry_over.val = node_sum // 10

                node_sum = node_sum % 10
            else:
                carry_over.val = 0

            curr.next = ListNode(node_sum)
            curr = curr.next
        
        
        return start.next