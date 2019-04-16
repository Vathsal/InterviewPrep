"""

Unordered List IMPLEMENTATION 

NODE : 
Each node must contain the list item itself, called the 'data' field of the node.
Each node must hold a reference to the next node, called the 'next' field of the node.
The Node class also includes the usual methods to access and modify the 'data' and the 'next' reference.

UNORDERED LIST :
The head of the list refers to the first node which contains the first item of the list. In turn, that node holds a reference to the next node (the next item) and so on. 
It is very important to note that the list class itself does not contain any node objects. 
Instead it contains a single reference to only the first node in the linked structure.
size, search, and remove – are all based on a technique known as linked list traversal. 

"""

class Node :
	def __init__(self,initalData) :
		self.data = initalData
		self.next = None

	def getData(self) :
		return self.data

	def setData(self,newData) :
		self.data = newData

	def getNext(self) :
		return self.next

	def setNext(self,newNext) :
		self.next = newNext



class UnorderedList :
	#constructor
	def __init__(self):
		self.head = None

	def add(self, item) :
		newNode = Node(item) #create a new node
		newNode.setNext(self.head) #head contains the reference to the latest node, so point the next to that
		self.head = newNode # point the head to this new node, as this is the latest node now 

"""
The remove method requires two logical steps. 
	1. Traverse the list looking for the item we want to remove. 
	2. Once we find the item (we assume it is present), we must remove it.

'current' starts out at the list head as in the other traversal examples. 
'previous', however, is assumed to always travel one node behind current. For this reason, previous starts out with a value of None since there is no node before the head. 
The boolean variable 'found' will again be used to control the iteration.
Next we ask whether the item stored in the current node is the item we wish to remove. 
	- If so, 'found' can be set to True. 
	- If we do not find the item, previous and current must both be moved one node ahead. 
	  Again, the order of these two statements is crucial. 
	  previous must first be moved one node ahead to the location of current. 
	  At that point, current can be moved. This process is often referred to as “inch-worming” as previous must catch up to current before current moves ahead. 
"""
	def remove(self,item) :
		current = self.head
		previous = None
		found = False 

		while current != None and not found :
			if current.getData() == item :
				found = True
			else :
				previous = current
				current = current.getNext()

		if previous == None :
			self.head = current.getNext()
		else :
			previous.setNext(current.getNext())


	def search(self,item) :
		current = self.head #start traversal at the head
		found = False 

		while current != None and not found :
			if current.getData() == item :
				found = True
			else : 
				current = current.getNext()

		return found


"""
To traverse the list, we use an external reference that starts at the first node in the list.
The external reference called current is initialized to the head of the list. 
At the start of the process we have not seen any nodes so the count is set to 0.
As long as the current reference has not seen the end of the list (None), we move current along to the next node. 
Every time current moves to a new node, we add 1 to count.
Finally, count gets returned after the iteration stops.
"""
	def size(self) :
		current = self.head
		count = 0 
		while current != None :
			current = current.getNext()
			count += 1

		return count 

	def isEmpty(self) :
		return self.head == None

	def index(self,item) :

	def append(self,item) :

	def insert(self,pos,item) :

	def pop(self) :

	def pop(self, pos) :
