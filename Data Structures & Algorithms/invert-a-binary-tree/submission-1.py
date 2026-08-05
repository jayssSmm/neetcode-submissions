# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        x = root
        q = queue()
        q.enqueue(root)

        while q.len() or p:
            p = q.dequeue()
            if not p:
                continue
            p.left, p.right = p.right, p.left
            q.enqueue(p.right)
            q.enqueue(p.left)

        return x

class queue:
    def __init__(self):
        self.q = []

    def enqueue(self, x):
        self.q.append(x)
    
    def dequeue(self):
        if len(self.q):
            return self.q.pop(0)
        return None
    
    def len(self):
        return len(self.q)