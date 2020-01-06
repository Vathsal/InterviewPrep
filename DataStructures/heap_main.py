"""
	MAIN PROGRAM 
"""

from heap.max_heap import max_heap
import random

print("*** Max Heap Implementation using Array ***")

values = random.sample(range(100), 10)
print(values)

h = max_heap()
for v in values :
	h.push(v)

while h.len() > 0:
	print(h.pop())


