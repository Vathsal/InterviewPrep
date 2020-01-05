"""
	MAIN PROGRAM 
"""

from stack.StackImplLinkedList import StackImplLinkedList
from stack.StackImplArray import StackImplArray
from queue.QueueImplArray import QueueImplArray
from deque.Deque import Deque

"""
#------ Stack : Array 

s1 = StackImplArray()
print("*** Stack Implementation using Array ***")
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

#------ Stack : LinkedList 

s2=StackImplLinkedList()
print("*** Stack Implementation using LinkedList ***")
print("isEmpty : ", s2.isEmpty())
s2.push(5)
s2.push('dreggy')
print("peek    : ", s2.peek())
s2.push(True)
print("isEmpty : ", s2.isEmpty())
s2.push(15.4)
print("pop     : ", s2.pop())
print("pop     : ", s2.pop())


"""
#------ Queue Test

q=QueueImplArray()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print("Size    : ", q.size())
print("Deque   : ", q.dequeue())
print("isEmpty : ", q.isEmpty())

"""
d=Deque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True) 
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
print(d.removeRear())
print(d.removeFront())
"""