# 226. Invert Binary Tree


class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # Print the tree
    def printTree(self):
        print(self.value)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

    def invertTree(self, root):
        if not root:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


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
 
n1.printTree()

n1.invertTree(n1)
print("\nInverted\n")

n1.printTree()
