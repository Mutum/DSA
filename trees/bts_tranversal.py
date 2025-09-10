class TreeNode:
    def __init__(self, val):
        self.val = val         # Value stored in the node
        self.left = None       # Pointer to left child
        self.right = None      # Pointer to right child

class Solution:
    # Recursive method for inorder traversal
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)               # Traverse left subtree
        print(root.val, end=" ")              # Visit current node
        self.inorder(root.right)              # Traverse right subtree

if __name__ == "__main__":
    # Create a sample BST:
    #         8
    #       /   \
    #      3     10
    #     / \      \
    #    1   6      14
    #       /
    #      4
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.right.right = TreeNode(14)

    it = Solution()
    print("Inorder Traversal (Sorted Order):")
    it.inorder(root)  # Expected output: 1 3 4 6 8 10 14
    print()
