# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        x = []
        def ino(root):
            if not root:
                return
            ino(root.left)
            x.append(root.val)
            ino(root.right)

        ino(root)
        
        min_d = x[1] - x[0]
        for i in range(2, len(x)):
            d = x[i] - x[i-1]
            if d < min_d:
                min_d = d


        return min_d
