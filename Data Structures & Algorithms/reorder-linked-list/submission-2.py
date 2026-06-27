# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        reorder = ListNode()
        curr = reorder
        i = 0

        fast = head
        slow = head
        last = None;

        while fast:
            fast = fast.next
            if i % 2 == 0:
                last = slow
                slow = slow.next
            i += 1
        last.next = None
        
        mid_last = slow
        if slow and slow.next:
            mid_next = slow.next
            mid_last.next = None
            while mid_next:
                temp = mid_next.next
                mid_next.next = mid_last
                mid_last = mid_next
                mid_next = temp
        mid = mid_last

        while head or mid:
            if head:
                curr.next = head
                head = head.next
                curr = curr.next
            if mid:
                curr.next = mid
                mid = mid.next
                curr = curr.next
        head = reorder.next