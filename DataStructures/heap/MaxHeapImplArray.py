"""
	This is an implementation for max_heap which is implmented using python LIST
"""
class MaxHeapImplArray:
	def __init__(self):
		self.heap = []

	def is_empty(self):
		return len(self.heap) == 0 

	def len(self): 
		return len(self.heap)

	# Insert a key into the max_heap
	def push(self, value): 
		self.heap.append(value)		
		_sift_up(self.heap, len(self.heap)-1)

	# Return the largest key from the max_heap
	def peek(self): 
		return self.heap[0]

	# Return and remove the largest key from the max_heap
	def pop(self): 
		if self.is_empty() :
			raise Exception("Heap is empty !")

		swap(self.heap, 0, len(self.heap)-1)
		max_value = self.heap.pop()
		_sift_down(self.heap, 0)
		return max_value 

def swap(myArray,i,j):
	myArray[i], myArray[j] = myArray[j], myArray[i]

def _sift_up(heap, current_index):
	parent_index = (current_index-1)//2
	# If we've hit the root node, there's nothing left to do
	if parent_index < 0 :
		return 

	# If the current node is larger than the parent node :
	# 	1. Swap the current node and parent node
	# 	2. Repeat by moving up until you restore the heap order
	if heap[current_index] > heap[parent_index]:
		swap(heap, current_index, parent_index)
		_sift_up(heap, parent_index)

def _sift_down(heap, current_index):
	# child_index     => left child 
	# child_index + 1 => right child 	
	child_index = 2*current_index + 1
	# If we've hit the end of the heap, there's nothing left to do 
	if child_index >= len(heap):
		return

	# If both the children are present and the parent is smaller than both children :
	# 	1. Swap the current node with the LARGER of the child nodes 
	# 	2. Repeat by moving down until you restore the heap order
	# If only one child is present and the parent is smaller than the child :
	# 	1. Swap the current node with the child node 
	# 	2. Repeat by moving up until you restore the heap order

	# Check if the right child is larger, if so assign that that the child to be swapped. 
	if child_index+1 < len(heap) and heap[child_index+1] > heap[child_index]:
		child_index += 1 

	if heap[child_index] > heap[current_index]:
		swap(heap, current_index, child_index)
		_sift_down(heap, child_index)
