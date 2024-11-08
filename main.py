class Node:
    # Constructor to initialize the node
    def __init__(self, value=None, next_node=None, previous_node=None):
        # Public properties
        self.value = value
        self.next = next_node
        self.previous = previous_node

    # Set the value of this node
    def set(self, value):
        self.value = value
        return self  # Return the current node

    # Get the value of this node
    def get_value(self):
        return self.value

    # Get the next node
    def get_next(self):
        return self.next

    # Get the previous node
    def get_previous(self):
        return self.previous

    # Set the next node
    def set_next(self, next_node):
        self.next = next_node
        return self  

    # Set the previous node
    def set_previous(self, previous_node):
        self.previous = previous_node
        return self


node1 = Node(10)
node2 = Node(20)

node1.set_next(node2)
node2.set_previous(node1)

print(node1.get_value())              
print(node1.get_next().get_value()) 
print(node2.get_previous().get_value())
