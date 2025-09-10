# Python: Using queue.Queue
from queue import Queue

queue = Queue()

queue.put(10)  # Enqueue
queue.put(20)
queue.put(30)
print("Front element:", queue.queue[0])  # Peek (Output: 10)

print("Dequeued:", queue.get())  # Dequeue (Output: 10)
print("Is Queue Empty?", queue.empty())  # Check if empty
