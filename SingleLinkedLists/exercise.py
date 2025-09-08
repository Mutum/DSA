
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class reverse_linked_list:

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None  # This will eventually become the new head
        current = head  # Start with the current node as the head

        while current:
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the link
           
            prev = current  # Move prev to the current node
            current = next_node  # Move to the next node in the original list

        return prev  # At the end, prev will be the new head

    @staticmethod
    def print_list(head):
        result = []
        current = head
        while current:
            result.append(current.value)
            current = current.next
        return result

# Helper function to print the linked list


# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

reverse = reverse_linked_list()

# Reverse the linked list
reversed_head = reverse.reverseList(head)
print(reverse.print_list(reversed_head))

restored_head = reverse.reverseList(reversed_head)

print(reverse.print_list(restored_head))

print(reverse.print_list(reversed_head)) # prints 4 


################ merge two sorted linked list


class Node :
    def  __init__(self, data):
        self.data = data
        self.next = None

class merge_sorted:
   
    def merge_sorted(self, llist1: Node, llist2: Node ) :

        # we are not handle any edge cases like empty link list
        # just focussing on merging part    
        current = llist1
        while current.next:  # Continue until we reach the last node
            current = current.next
            
        # Connect the last node to the second list
        current.next = llist2
        
        return llist1


llink1 = Node(1)
llink1.next = Node(5)
llink1.next.next = Node(7)

llink2 = Node(9)
llink2.next = Node(10)
llink2.next.next = Node(11)

linked_merge = merge_sorted()
linked_merge.merge_sorted(llink1, llink2)

