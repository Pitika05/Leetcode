# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(node, result):
            if node==None:
                return
            
            result.append(node.val)
            preorder(node.left, result)
            preorder(node.right, result)

        result=[]
        preorder(root, result)
        return result