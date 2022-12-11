# 543 Diameter of Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def diameterOfBinaryTree(self, root) -> int:
        self.maxL = 0

        def dfs(root):
            if not root:
                return 0
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                self.maxL = max(self.maxL, left + right)

            return 1 + max(left, right)

        dfs(root)
        return self.maxL



n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

print(n1.diameterOfBinaryTree(n1))
