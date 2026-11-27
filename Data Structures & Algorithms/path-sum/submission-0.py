# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        y = targetSum
        def pre(root, y):
            if not root:
                return False

            y -= root.val

            if not root.left and not root.right:
                return y == 0

            return pre(root.left, y) or pre(root.right, y)

        return pre(root, y)