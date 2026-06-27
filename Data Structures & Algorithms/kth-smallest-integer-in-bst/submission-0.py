# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        smallest = []

        def in_order(root):
            if not root:
                return
            
            if (root.left):
                in_order(root.left)

            if len(smallest) >= k:
                return
            smallest.append(root)

            if root.right:
                in_order(root.right)

        in_order(root)
        return smallest.pop().val
