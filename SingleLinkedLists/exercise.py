
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
