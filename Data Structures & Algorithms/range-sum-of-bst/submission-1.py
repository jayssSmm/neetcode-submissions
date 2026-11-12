# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        x = []
        def ino(root):
            if not root:
                return

            ino(root.left)
            x.append(root.val)
            ino(root.right)

        ino(root)
        if x[-1] < low:
            return 0
        i, j = 0, len(x) - 1
        while (i<=j):
            if x[i] < low:
                i+=1
            if x[j] > high:
                j-=1
            if x[i] >= low and x[j] <= high:
                j+=1
                break

        x = x[i: j]
        return sum(x)