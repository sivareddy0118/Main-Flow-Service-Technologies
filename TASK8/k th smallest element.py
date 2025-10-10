# Program to find K-th smallest element in BST using Inorder Traversal
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root, elements):
    if not root:
        return
    inorder(root.left, elements)
    elements.append(root.val)
    inorder(root.right, elements)

def kth_smallest(root, k):
    elements = []
    inorder(root, elements)
    return elements[k - 1]

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)

print("3rd Smallest Element:", kth_smallest(root, 3))
