# 872 Leaf-Similar Trees

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Print the tree
    def printTree(self):
        print(self.val)
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

    def leafSimilar(self, root1, root2) -> bool:
        pstack = []
        qstack = []

        def dfs(root, stack):
            if not root:
                return

            # If leaf, append value
            if not root.left and not root.right:
                stack.append(root.val)

            dfs(root.left, stack)
            dfs(root.right, stack)

        dfs(root1, pstack)
        dfs(root2, qstack)

        print(pstack)
        print(qstack)

        return pstack == qstack


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print("N")
n1.printTree()

m1 = TreeNode(1)
m2 = TreeNode(2)
m3 = TreeNode(3)
m1.left = m3
m1.right = m2
print("M")
m1.printTree()