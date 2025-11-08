class BinaryTree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.parent = None


root = BinaryTree(10)
root.left = BinaryTree(5)
print(root.key, root.left.key, root.right)

def print_keys(node):
    print(node.key)
    if node.left:
        print(node.left.key)
    if node.right:
        print(node.right.key)