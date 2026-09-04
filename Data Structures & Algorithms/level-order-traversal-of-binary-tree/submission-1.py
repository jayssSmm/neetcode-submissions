# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        layers = []
        layer = [root]
        while layer:
            next_layer = []
            for i in layer:
                if i:
                    next_layer.append(i.left)
                    next_layer.append(i.right)

            layers.append([i.val for i in layer if i])
            layer = next_layer

        return layers[:-1]

        