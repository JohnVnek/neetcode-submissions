# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        curr = merged

        one = list1
        two = list2
        while one and two:
            if one.val > two.val:
                curr.next = two
                two = two.next
            else:
                curr.next = one
                one = one.next
            curr = curr.next
        if one:
            curr.next = one
        if two:
            curr.next = two
        return merged.next
