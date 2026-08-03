# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st=[]
        l=[]
        while root or st:
            if root:
                l.append(root.val)
                st.append(root)
                root = root.left
            else:
                root = st.pop()
                root = root.right

        return l