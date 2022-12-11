# 110 - Balanced Binary Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isBalanced(self, root) -> bool:
        maxH = 1

        if not root:
            return True

        def dfs(root) -> int:
            nonlocal maxH

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            maxH = max(maxH, max(left, right) - min(left, right))

            return 1 + max(left, right)

        dfs(root)

        return maxH == 1


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n6 = TreeNode(30)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
n4.right = n6

print(n1.isBalanced(n1))
