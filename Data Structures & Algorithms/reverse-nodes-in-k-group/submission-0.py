# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode()
        w = res

        def reverse(head):
            curr = head
            next_node = curr.next

            curr.next = None

            while next_node:
                after = next_node.next
                next_node.next = curr
                curr = next_node
                next_node = after

        curr = head
        fast = curr
        after = curr
        while fast:
            count = 0
            for i in range(k-1):
                if fast.next:
                    fast = fast.next
                    count += 1


            after = fast.next
            fast.next = None
            if count == k-1:
                reverse(curr)
                w.next = fast
                w = curr
                
                curr = after
                fast = after
            else:
                w.next = curr
                break

        return res.next

        
