# Program for Zigzag Level Order Traversal

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def zigzag_traversal(root):
    if not root:
        return []
    result, current, left_to_right = [], [root], True
    while current:
        level = [node.val for node in current]
        if not left_to_right:
            level.reverse()
        result.append(level)
        next_level = []
        for node in current:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        current = next_level
        left_to_right = not left_to_right
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print("Zigzag Level Order Traversal:", zigzag_traversal(root))
