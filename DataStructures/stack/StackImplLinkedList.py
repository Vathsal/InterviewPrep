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

	# 1. Create a Node object using the value provided
	# 2. Assign it to the head
	def push(self,item):
		value = item
		nextNode = self.head
		self.head = Node(value, nextNode) 

	# 1. Save the value that you need to return
	# 2. Delete the first node and assign nextNode to head
	# 3. Return the saved value  
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

	# def size(self):
		# TODO 

	def isEmpty(self):
		return self.head is None

