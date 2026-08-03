# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l, m = [], []
        while p or l or q:
            if not p:
                if q:
                    return False
                p = l.pop()
                p = p.right

                q = m.pop()
                q = q.right
            else:
                if (q and p==None) or (q==None and p):
                    return False
                if (p.val!=q.val):
                    return False
                l.append(p)
                m.append(q)
                p = p.left
                q = q.left

        return True
                