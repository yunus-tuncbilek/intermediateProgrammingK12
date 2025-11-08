class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Pointer to the next node, initially None
        # self.name = "Node"

    def __str__(self):
        return f"Node({self.value})"
    
    def last(self): # class method to find the last node
        temp = self
        while temp.next is not None:
            temp = temp.next
        return temp

# x = Node(5)
# y = Node(10)
# z = Node(15)
# h = Node(20)

# x.next = y # attach y to x
# y.next = z # attach z to y
# z.next = h # attach h to z

# # temp = x

# # while temp.next is not None:
# #     temp = temp.next

# # print(temp)  # Should print the last Node

# print(x.last())  # Should print the last Node using the last() method



class LinkedList:
    def __init__(self):
        self.head = None  # Pointer to the first node
        self.tail = None  # Pointer to the last node (optional, but useful for O(1) appends)
        self.length = 0   # Keeps track of the number of nodes

    def append(self, value):
        # Time Complexity: O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        # Time Complexity: O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        # Time Complexity: O(n), except when inserting at head or tail which is O(1)
        if index < 0 or index > self.length:
            print("Invalid index")
            return
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return

        new_node = Node(value)
        temp_node = self.get_node(index - 1)
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1

    def get_node(self, index):
        # Time Complexity: O(n)
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def traverse(self):
        # Time Complexity: O(n)
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def remove(self, index):
        # Time Complexity: O(n), except when removing the head which is O(1)
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            popped_node = self.head
            self.head = self.head.next
            if self.head is None: # If list becomes empty after removal
                self.tail = None
            popped_node.next = None
            self.length -= 1
            return popped_node.value
        
        prev_node = self.get_node(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        if popped_node == self.tail: # If removing the tail
            self.tail = prev_node
        popped_node.next = None
        self.length -= 1
        return popped_node.value

    def search(self, value):
        # Time Complexity: O(n)
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == value:
                return index
            current_node = current_node.next
            index += 1
        return -1  # Value not found
    
# Example usage:

my_linked_list = LinkedList()

# Append values to the linked list
my_linked_list.append(10)
my_linked_list.append(20)
my_linked_list.append(30)

# Traverse the linked list
my_linked_list.traverse()

# # Remove the head node
my_linked_list.remove(0)

# # Traverse again to see the updated list
my_linked_list.traverse()


my_linked_list.insert(1, 15)

my_linked_list.traverse()

my_linked_list.prepend(5)

my_linked_list.traverse()

id = my_linked_list.search(20)
if id != -1:
    print("Index of value 20:", id)
else:
    print("Value 20 not found in the list")