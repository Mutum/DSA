# A linked list is a linear data structure consisting of a sequence of
# element call nodes, where each node contain two part
# 1. data – The value stored in the node.
# 2. Pointer (Next Reference) – A reference to the next node in the list.

# A linked list always has a starting point (Head) and may have an ending point (Tail), depending on the type of linked list. If a node does not point to another node, its reference is set to NULL

# Types :
# Singly Linked List - each node points to next
# Doubly Linked List - each node points to next and previous node
# Circular Linked List - last node connects back to first node

# Singly Linked List Transversal

# Class to define a Node
class Node:
    def __init__(self, val):
        self.val = val  # Data stored in the node
        self.next = None  # Pointer to the next node


# Linked List class with traversal method
class Solution:
    def __init__(self):
        self.head = None  # Head pointer to the linked list

    # Traversal method to print all elements
    def traverse(self):
        current = self.head  # Start from the head node
        while current:
            print(current.val, end=" → ")  # Print current node value
            current = current.next  # Move to the next node
        print("NULL")  # Indicate end of the list


link_list = Solution()

# Creating linked list: 10 → 20 → 30 → 40 → NULL
link_list.head = Node(10)
link_list.head.next = Node(20)
link_list.head.next.next = Node(30)
link_list.head.next.next.next = Node(40)

# Perform traversal
print("Linked List Traversal:")
link_list.traverse()

