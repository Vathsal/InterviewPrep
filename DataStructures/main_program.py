"""
MAIN PROGRAM 
"""

from Stack import Stack
from Queue import Queue
from Deque import Deque

"""
#------ Stack Test

s=Stack()

print "Is list empty ? :" , s.isEmpty()
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

#------ Queue Test

q=Queue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.dequeue())

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