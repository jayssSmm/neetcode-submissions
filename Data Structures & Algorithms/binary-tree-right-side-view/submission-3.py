# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        layers = []
        layer = [root]

        while layer:
            next_layer = []
            for i in layer:
                if i:
                    if i.left:
                        next_layer.append(i.left)
                    if i.right:
                        next_layer.append(i.right)
                    
            layers.append(layer[-1].val)
            layer = next_layer

        return layers
