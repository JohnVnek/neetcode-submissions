# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if head == None:
            return head

        curr = head
        count = 0
        while curr != None:
            count += 1
            curr = curr.next

        target = count - n

        last = None
        node = head
        idx = 0

        print(target)

        while idx != target:
            last = node
            node = node.next
            idx += 1


        if last == None:
            return head.next
        last.next = node.next

        return head


        