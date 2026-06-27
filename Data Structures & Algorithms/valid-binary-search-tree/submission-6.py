# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkBST(root, left_bound, right_bound):
            if not root:
                return True

            in_bounds = left_bound < root.val < right_bound

            return (in_bounds and checkBST(root.left, left_bound, min(root.val, right_bound)) and checkBST(root.right, max(root.val, left_bound), right_bound))

        return checkBST(root, float('-inf'), float('inf'))