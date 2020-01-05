"""
	Queue Implementation using LinkedList
	Stack implmentation in Python which only uses a head pointer to the linked list, the Queue implementation contains both a head and tail pointer of the linked list. 
	By maintaining a head and tail pointer in the linked list, we are able to guarantee that enqueue and dequeue are constant time O(1) operations.
"""

class Node:
	def __init__(self, value, nextNode = None):
		self.value = value
		self.nextNode = nextNode

class QueueImplLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def enqueue(self,item):
		value = item
		nextNode = self.head

		if self.head is None:
			self.head = Node(value, nextNode)
			self.tail = self.head
			return 

		self.tail.nextNode = Node(value, nextNode)
		self.tail = Node(value, nextNode)

	def dequeue(self):
		if self.isEmpty():
			raise Exception("Queue is empty")
		value = self.head.value
		self.head = self.head.nextNode

		if self.head is None:
			self.tail = None

		return value

	# def size():
		# TODO 

	def isEmpty(self):
		return self.head is None



