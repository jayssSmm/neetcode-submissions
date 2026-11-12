# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        l = [root, None]
        flag = True

        while l:
            p = l[0]
            l = l[1:]
            #print(l)

            if not p:
                if not l:
                    return True

                for i in l:
                    if i == 'c':
                        flag = False
                    else:
                        if not flag:
                            return False
                        flag = True

                l.append(None)
                continue

            if p != 'c':
                if p.left:
                    l.append(p.left)
                else:
                    l.append('c')
                if p.right:
                    l.append(p.right)
                else:
                    l.append('c')

