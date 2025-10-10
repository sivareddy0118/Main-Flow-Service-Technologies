# Serialize and Deserialize a Binary Tree using Preorder Traversal

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def serialize(root):
    if not root:
        return "None,"
    return str(root.val) + "," + serialize(root.left) + serialize(root.right)

def deserialize(data):
    values = data.split(',')
    def helper():
        val = values.pop(0)
        if val == "None" or val == "":
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node
    return helper()

# Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

data = serialize(root)
print("Serialized Tree:", data)
tree = deserialize(data)
print("Deserialized Root Value:", tree.val)
