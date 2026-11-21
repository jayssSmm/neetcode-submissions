# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        q = deque()
        q.append(root)
        q.append(None)

        while q:
            #print(q)
            p = q.popleft()

            if not p:
                if not q:
                    break

                for i in range(len(q)//2):
                    j = len(q)-i-1
                    if type(q[i]) != type(q[j]):
                        return False
                    else:
                        #print("esle",type(q[i]), type(q[j]))
                        if isinstance(q[i], TreeNode):
                            if q[i].val != q[j].val:
                                return False
                        else:
                            if q[i] != q[j]:
                                return False

                q.append(None)
                continue
            if type(p) == str:
                continue

            if p.left:
                q.append(p.left)
            else:
                q.append('c')
            
            if p.right:
                q.append(p.right)
            else:
                q.append('c')

        return True