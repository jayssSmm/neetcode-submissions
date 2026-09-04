# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class queue:
    def __init__(self):
        self.l = []
        self.head = 0
        self.tail = -1

    def display(self):
        for i in self.l:
            if i:
                print(i.val, end = ' ')
            else:
                print("None", end = ' ')

    def enqueue(self, x):
        self.l.append(x)
        self.tail+=1

    def dequeue(self):
        if self.tail<0:
            return -1
        x = self.l[self.head]
        self.head+=1
        return x

    def lenght(self):
        return self.tail-self.head

    def layer(self):
        result = []
        current = []
        for item in self.l[:self.tail]:
            if item is None:
                result.append(current)
                current = []
            else:
                current.append(item.val)

        return result

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        p = root
        q = queue()

        q.enqueue(p)
        q.enqueue(None)

        while p or q.lenght():
            p = q.dequeue()
            if not p:
                q.enqueue(None)
                continue
            if p.left:
                q.enqueue(p.left)
            if p.right:
                q.enqueue(p.right)
                
        return q.layer()

        