"""

QUEUE IMPLEMENTATION 

Implemented using LISTS 
This implementation assumes that the rear is at position 0 in the list. 
ENQUEUE : add item at position 0. O(n)
DEQUE : remove item from position n. O(1)

"""
class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []