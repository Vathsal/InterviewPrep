"""
	Main Program for Heap Implementation :
		1. Max_heap 
		2. Min_heap
"""
from heap.max_heap import max_heap
from heap.min_heap import min_heap
import random

values = random.sample(range(100), 10)
print("Input array : ")
print(values)

print("Max Heap Implementation using Array : ")
h1 = max_heap()
for v in values :
	h1.push(v)

while h1.len() > 0:
	print(h1.pop(), end=' ')

print()


print("Min Heap Implementation using Array : ")
h2 = min_heap()
for v in values :
	h2.push(v)

while h2.len() > 0:
	print(h2.pop(), end=' ')

print()