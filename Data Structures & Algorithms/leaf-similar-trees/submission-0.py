# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        x = []
        y = []
        def leaf(root, x):
            if not root:
                return

            if not root.left and not root.right:
                x.append(root.val)
            
            leaf(root.left, x)
            leaf(root.right, x)

        leaf(root1, x)
        leaf(root2, y)

        return x == y