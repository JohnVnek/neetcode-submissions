"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Iterate through original list
        # For each copied node, create map with key = org_node, val = new_node

        # Iterate through original list & new list

        if head == None:
            return None

        node_map = {}

        curr = head

        copy_head = Node(head.val)
        copy = None

        while curr != None:
            if curr == head:
                copy = copy_head
            else:
                copy.next = Node(curr.val)
                copy = copy.next
            node_map[curr] = copy
            curr = curr.next

        curr = head
        copy = copy_head

        while curr != None:
            if curr.random == None:
                copy.random == None
            else:
                copy.random = node_map[curr.random]
            copy = copy.next
            curr = curr.next
        return copy_head

