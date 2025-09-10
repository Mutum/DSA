# A stack is a linear data structure that follows the Last-In, First-Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed.

# Basic Stack Operations
# A stack provides four fundamental operations:

# Push → Adds an element to the top of the stack.
# Pop → Removes the topmost element from the stack.
# Peek (or Top) → Returns the topmost element without removing it.
# IsEmpty → Checks if the stack is empty.
# IsFull → Checks if the stack is full.

# Fundamental implementation of stack with list


class Stack:
    """Implementation of stack with pyton built-in list"""

    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def get_stack(self):
        return self.stack

    def clear(self):
        self.stack.clear()


myStack = Stack()
myStack.push("A")
myStack.push("B")
print(myStack.get_stack())
myStack.push("C")
print(myStack.get_stack())
myStack.pop()
print(myStack.get_stack())
print(myStack.size())
print(myStack.is_empty())

# Monotonic stacks
# A monotonic stack is a stack that maintains its elements in either increasing or decreasing order.
# This means that as new element are pushed onto the stacks , elements that break
# the order are removed before the new element is added

# A monotonic increasing stack is a stack where the elements are arranged in increasing order from bottom to top. When a new element is pushed onto the stack, elements that are greater than the new element are popped off to maintain the monotonic property.


class MonotonicIncreasingStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        # if stack not empty and element greater than the value
        while self.stack and self.stack[-1] > value:
            # remove all element greater than the value
            self.stack.pop()

        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def top(self):
        """view top element"""
        if self.stack:
            return self.stack[-1]
        return None

    def get_stack(self):
        return self.stack


# Create a monotonic increasing stack
stack = MonotonicIncreasingStack()

# Push elements onto the stack
stack.push(10)
stack.push(5)
stack.push(8)
stack.push(3)

# Display the stack
stack.get_stack()  # Output: Monotonic Increasing Stack (bottom to top): [3]

# Peek at the top element
print("Top element is:", stack.top())  # Output: Top element is: 3

# Pop an element
stack.pop()  # Output: Popped 3 from the stack.

# Display the stack again
stack.get_stack()
