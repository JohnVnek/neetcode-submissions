# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compTrees(tree, subTree):
            if not tree and not subTree:
                return True
            if not tree or not subTree:
                return False
            # print("tree " + str(tree.val))
            # print("subtree " + str(subTree.val))
            if tree.val != subTree.val:
                return False
            return compTrees(tree.left, subTree.left) and compTrees(tree.right, subTree.right)
        
        
        if not root and not subroot:
            return True
        if not root:
            return False
        stack = [root]

        while stack:
            curr = stack.pop()
            if curr:
                # print("curr " + str(curr.val))

                if curr.val == subRoot.val:
                    if compTrees(curr, subRoot):
                        return True
                stack.append(curr.left)
                stack.append(curr.right)
        return False

        