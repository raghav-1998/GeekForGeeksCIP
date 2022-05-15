# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root, level):
            if not root:
                return 
            if not root.left and not root.right:
                if level > self.max_level:
                    self.max_level = level
                    self.ans = root.val
                elif level == self.max_level:
                    self.ans += root.val      
                return
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            return
        
        self.max_level, self.ans = -1, 0
        dfs(root , 0)
        return self.ans