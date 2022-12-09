# 104. Maximum Depth of Binary Tree


class Node:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    # Print the tree
    def printTree(self) -> None:
        print(self.value)
        if self.left:
            self.left.printTree()
        else:
            print(None)
        if self.right:
            self.right.printTree()
        else:
            print(None)

    def maxDepth(self, root) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# Sample Tree
n1 = Node(3)
n2 = Node(9)
n3 = Node(20)
n4 = Node(15)
n5 = Node(7)
n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

n1.maxDepth(n1)

n1.printTree()
