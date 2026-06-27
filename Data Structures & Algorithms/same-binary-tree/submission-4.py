# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False

        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_q:
            curr_p = stack_p.pop()
            curr_q = stack_q.pop()

            if curr_p is None and curr_q is None:
                continue
            if curr_p is None or curr_q is None:
                return False
            if curr_p.val != curr_q.val:
                return False
            stack_p.append(curr_p.left)
            stack_p.append(curr_p.right)
            stack_q.append(curr_q.left)
            stack_q.append(curr_q.right)

        return True
