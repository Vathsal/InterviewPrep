"""
MAIN PROGRAM 
"""

from stack.Stack import Stack
from queue.Queue import Queue
from deque.Deque import Deque


#------ Stack Test

s=Stack()

print("isEmpty : ", s.isEmpty())
s.push(5)
s.push('dreggy')
print("peek    : ", s.peek())
s.push(True)
print("size    : ", s.size())
print("isEmpty : ", s.isEmpty())
s.push(15.4)
print("pop     : ", s.pop())
print("pop     : ", s.pop())
print("size    : ", s.size())

"""
#------ Queue Test

q=Queue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.dequeue())


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
