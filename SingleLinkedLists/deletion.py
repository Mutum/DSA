# Takes the Insertion.py and extends the code for deletion

# Deletion by Value
# To solve this problem, we need to handle two cases:

# Node to be deleted is head.
# Node to be deleted is not head.

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

    def delete_node(self, key):

        # deleted node in case it is head    
        cur_node = self.head

        if cur_node and cur_node.data == key :
            self.head = cur_node.next
            cur_node = None
            return 
        
        # if not deletion is at head position
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next 

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None
    
    def delete_nodeAtPostion(self, position):

        if position == 0:
            current = self.head
            self.head = current.next
            current = None
            return

        # find previous node just before the position
        pred = self.head

        for i in range(position -1 ):
            if pred is None:
                print('invalid position')
                return
            pred  = pred.next
        
        if pred is None:
            print("Invalid position")
            return
        
        # lets delete
        to_delete_node = pred.next
        replacement_node = to_delete_node.next

        pred.next = replacement_node
        to_delete_node = None

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
link_list.delete_node(25)
link_list.tranverse()
link_list.delete_nodeAtPostion(2)
link_list.tranverse()