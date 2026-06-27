# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        nodes = deque()
        children = deque()

        nodes.append(root)
        while nodes:
            curr = nodes.popleft()
            if curr.left:
                children.append(curr.left)
            if curr.right:
                children.append(curr.right)
            if not nodes:
                nodes = children
                children = deque()

                res.append(curr.val)
        return res

