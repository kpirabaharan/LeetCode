# 104. Maximum Depth of Binary Tree

class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def maxDepth(self, root):
        if not root:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1 + self.maxDepth(root.right)

        return max(left, right)


n1 = Node(3)
n2 = Node(9)
n3 = Node(20)
n4 = Node(15)
n5 = Node(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

print(n1.maxDepth(n1))
