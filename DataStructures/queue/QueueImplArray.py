"""
	QUEUE Implementation using Array (i.e LIST in python) 
	This implementation assumes that the rear is at position 0 in the list. 
		ENQUEUE : add item at position 0. 		T = O(n)
		DEQUE   : remove item from position n. 	T = O(1)
"""

class QueueImplArray:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)
		# self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop(0)
		# return self.items.pop()

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return len(self.items) == 0