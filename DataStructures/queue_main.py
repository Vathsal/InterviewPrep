"""
	Main Program for :
		1. Queue implementation using Array 
		2. Queue implementation using LinkedList 
"""
from queue.QueueImplArray import QueueImplArray
from queue.QueueImplLinkedList import QueueImplLinkedList

print("*** Queue Implementation using Array ***")
q1=QueueImplArray()

q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)
print("Size    : ", q1.size())
print("Deque   : ", q1.dequeue())
print("isEmpty : ", q1.isEmpty())

print("*** Queue Implementation using LinkedList ***")
q2= QueueImplLinkedList()

q2.enqueue(1)
q2.enqueue(2)
q2.enqueue(3)
q2.enqueue(4)
q2.enqueue(5)
print("Deque   : ", q2.dequeue())
print("isEmpty : ", q2.isEmpty())
