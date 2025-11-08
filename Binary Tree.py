class BinaryTree:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.parent = None

root = BinaryTree(10)
root.left = BinaryTree(5)
root.right = BinaryTree(11)
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(12)

# recursive solution to 10.4-2
def print_keys(node):
    print(node.key)
    if node.left:
        print_keys(node.left)
    if node.right:
        print_keys(node.right)

def print_keys_iter(node):
    stack = [node]

    while stack:
        x = stack.pop()

        print(x.key)
        
        if x.right:
            right_x = x.right
            stack.append(right_x)
        if x.left:
            left_x = x.left
            stack.append(left_x)
        

print_keys(root)  