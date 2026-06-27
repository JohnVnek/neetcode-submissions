# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists and len(lists) == 0:
            return None

        def mergeLists(list1, list2):
            res = ListNode()
            curr = res
            u = list1
            w = list2

            while u and w:
                if u.val < w.val:
                    curr.next = u
                    u = u.next
                else:
                    curr.next = w
                    w = w.next
                curr = curr.next
            if u:
                curr.next = u
            if w:
                curr.next = w
            return res.next

        res = lists[0]
        for i in range(1, len(lists)):
            res = mergeLists(res, lists[i])

        return res