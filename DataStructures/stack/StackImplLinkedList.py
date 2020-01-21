"""
	STACK Implementation using LinkedList 
"""

class Node :
	def __init__(self, value, nextNode = None):
		self.value = value
		self.nextNode = nextNode

class StackImplLinkedList :
	def __init__(self):
		self.head = None

	def push(self,item):
		self.head = Node(value, self.head) 

	def pop(self):
		if self.isEmpty():
			raise Exception("Stack is empty")
		value = self.head.value
		self.head = self.head.nextNode
		return value

	def peek(self):
		if self.isEmpty():
			raise Exception("Stack is empty")
		return self.head.value

	def isEmpty(self):
		return self.head is None

