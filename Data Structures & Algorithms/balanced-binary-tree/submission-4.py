# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def height(root):
            if not root:
                return 0, True
            x = height(root.left)
            y = height(root.right)

            if not x[1]:
                return x[0],False
            elif not y[1]:
                return y[0],False

            x, y = x[0], y[0]

            if x-y>1 or x-y<-1:
                return 0,False
            return max(x, y)+1, True

        return height(root)[1]