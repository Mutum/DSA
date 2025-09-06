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
class tranverse_list:
    def __init__(self):
        self.head = None  # Head pointer to the linked list

    # Traversal method to print all elements
    def traverse(self):
        current = self.head  # Start from the head node
        while current:
            print(current.val, end=" → ")  # Print current node value
            current = current.next  # Move to the next node
        print("NULL")  # Indicate end of the list


link_list = tranverse_list()

# Creating linked list: 10 → 20 → 30 → 40 → NULL
link_list.head = Node(10)
link_list.head.next = Node(20)
link_list.head.next.next = Node(30)
link_list.head.next.next.next = Node(40)

# Perform traversal
print("Linked List Traversal:")
link_list.traverse()

# Insertion (Adding a node at the beginning, end, or middle)
# Insertion is the process of adding a new node at a specified position in a linked list. Since linked lists are dynamically allocated, insertion does not require shifting elements (as in arrays), but it requires updating pointers correctly.

# We can insert a node at:

# The Beginning (Head Insertion) – Quickest insertion, updates the head pointer.
# The End (Tail Insertion) – Requires traversal to the last node.
# A Specific Position (Middle Insertion) – Requires traversal to find the correct location.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # add node to the end
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        # if not empty
        last_node = self.head  # initially its first node, we need to tranverse

        # transverse till the end
        while last_node.next:
            last_node = last_node.next

        # update with the required value
        last_node.next = new_node

    def prepend(self, data):
        # add node to the beginning
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        new_node.next = (
            self.head
        )  # point the next of the new_node to the current head of the linked list
        self.head = new_node  # set head of the linked list equal to new_node

    def insert_after_node(self, prev_node, data):
        """Insert a node after a given node """

        # check if prev node is none
        if not prev_node:
            print("Invalid previous node")
            return

        # check if pred node is part of the link list
        # if yes do the insertion
        current_node = self.head

        while current_node:
            if current_node.data == prev_node.data:
                new_node = Node(data)

                new_node.next = prev_node.next
                prev_node.next = new_node

                return

            current_node = current_node.next

        print("Previous node not in the linked list ")

    def insertAtPosition(self, data, position):
        new_node = Node(data)

        if position == 0 :
            self.head = new_node
            return 
        
        # need to find the node just prior to the position
        previous = self.head

        for i in range(position -1):
            if previous is None:
                print('Invalid position')
                return
            previous = previous.next

        next_node = previous.next

        previous.next = new_node
        new_node.next = next_node

    def tranverse(self):
        current = self.head

        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("Null")

link_list = LinkedList()
link_list.append("1")
link_list.append("2")
link_list.append("3")
link_list.append("4")
link_list.tranverse()
link_list.prepend("0")
link_list.tranverse()
link_list.insert_after_node(link_list.head.next, "D")
link_list.tranverse()
link_list.insertAtPosition(25, 2)
link_list.tranverse()
