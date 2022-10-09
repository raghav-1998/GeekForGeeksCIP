class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st):
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)

        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False