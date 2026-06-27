# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        nodes = []

        num = 1
        count = 0
        level = []
        while queue:
            curr = queue.popleft()
            print(curr.val)
            level.append(curr.val)
            count += 1
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

            if count == num:
                print("enter")
                num = len(queue)
                count = 0
                nodes.append(level)
                level = []
        return nodes

            
            

