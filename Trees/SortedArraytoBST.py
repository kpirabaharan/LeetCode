# 108 - Convert Sorted Array to Binary Search Tree
from typing import List, Optional


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


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    l, r = 0, len(nums) - 1

    def addNode(root, l, r):
        m = (l + r) // 2
        root = TreeNode(nums[m])
        if l <= m - 1:
            root.left = addNode(root.left, l, m - 1)
        if r >= m + 1:
            root.right = addNode(root.right, m + 1, r)

        return root

    top = addNode(TreeNode(nums[l + r // 2]), l, r)

    return top


nums = [-10, -3, 0, 5, 9]
node = sortedArrayToBST(nums)
node.printTree()
