# 102 Binary Tree Level Order Traversal
from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def levelOrder(self, root) -> List[List[int]]:
        q = []
        res = []
        l = 0

        def visit(root, level):
            nonlocal q
            nonlocal res

            if not root:
                return

            if len(res) <= level:
                res.append([root.val])
            else:
                res[level].append(root.val)

            q.append([root.left, level + 1])
            q.append([root.right, level + 1])

            return

        visit(root, l)

        while len(q) != 0:
            popped = q.pop(0)
            visit(popped[0], popped[1])

        return res


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)
n6 = TreeNode(6)
n7 = TreeNode(8)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
n2.left = n6
n2.right = n7

print(n1.levelOrder(n1))
