# 94 Binary Tree Inorder Traversal
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def InorderTraversal(self, root) -> List[int]:
        stack = []

        def dfsInorder(r, s):
            if r:
                dfsInorder(r.left, s)
                s.append(r.val)
                dfsInorder(r.right, s)

        dfsInorder(root, stack)

        return stack


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.right = n2
n2.left = n3

print(n1.InorderTraversal(n1))
