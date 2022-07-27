# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr=root
        
        while(curr!=None):
            if(curr.left!=None):
                prev=curr.left
                while(prev.right!=None):
                    prev=prev.right
                prev.right=curr.right
                curr.right=curr.left
                curr.left=None
            curr=curr.right