"""
	Main Program for :
		1. Stack implementation using Array 
		2. Stack implementation using LinkedList 
"""
from stack.StackImplLinkedList import StackImplLinkedList
from stack.StackImplArray import StackImplArray

print("*** Stack Implementation using Array ***")
s1 = StackImplArray()

print("isEmpty : ", s1.isEmpty())
s1.push(5)
s1.push('dreggy')
print("peek    : ", s1.peek())
s1.push(True)
print("size    : ", s1.size())
print("isEmpty : ", s1.isEmpty())
s1.push(15.4)
print("pop     : ", s1.pop())
print("pop     : ", s1.pop())
print("size    : ", s1.size())


print("*** Stack Implementation using LinkedList ***")
s2=StackImplLinkedList()

print("isEmpty : ", s2.isEmpty())
s2.push(5)
s2.push('dreggy')
print("peek    : ", s2.peek())
s2.push(True)
print("isEmpty : ", s2.isEmpty())
s2.push(15.4)
print("pop     : ", s2.pop())
print("pop     : ", s2.pop())
