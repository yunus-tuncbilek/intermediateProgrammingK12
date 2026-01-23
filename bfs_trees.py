class TreeNode:
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right     

from collections import deque

def tree_bfs(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        # Get the node that has been in the queue the longest
        node = queue.popleft()
        result.append(node.val)

        # Add children to the back of the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result

# Example usage:
# Constructing a simple binary tree:
#         Alice
#        /      \
#       Bob   Charlie 
#      /    \       \
#     David   Eve  Frank
root = TreeNode("Alice")
root.left = TreeNode("Bob")
root.right = TreeNode("Charlie")
root.left.left = TreeNode("David")
root.left.right = TreeNode("Eve")
root.right.right = TreeNode("Frank")

print(tree_bfs(root))  # Output: ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']


# What would be different in the case of BFS with a general graph?
# In a general graph, we need to keep track of visited nodes to avoid cycles.
def graph_bfs(start_node):
    visited = set()
    result = []
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        if node == None:
            continue
        result.append(node.val)
        for neighbor in node.neighbors:  # Assuming each node has a 'neighbors' attribute
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result