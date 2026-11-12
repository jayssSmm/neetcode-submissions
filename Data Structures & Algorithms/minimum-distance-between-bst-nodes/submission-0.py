# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
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
        if len(x) == 1:
            return x[0]
        min_d = x[1] - x[0]
        for i in range(2, len(x)):
            d = x[i] - x[i-1]
            if d < min_d:
                min_d = d


        return min_d
