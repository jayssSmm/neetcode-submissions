# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        def rec(root):
            if not root:
                return 0
            self.d = max(self.d, rec(root.left) + rec(root.right)) 
            return max(rec(root.left), rec(root.right))+1

        rec(root)
        return self.d