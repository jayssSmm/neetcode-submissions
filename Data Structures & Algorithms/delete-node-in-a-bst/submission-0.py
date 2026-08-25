# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preSuc(self, root): #left ka right
        while root.right:
            root = root.right
        return root
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val > key:
            root.left = self.deleteNode( root.left, key)
        elif root.val < key:
            root.right = self.deleteNode( root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right

            x = self.preSuc(root.left)
            root.val = x.val
            root.left = self.deleteNode(root.left, x.val)

        return root
                    