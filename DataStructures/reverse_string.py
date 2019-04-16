"""
REVERSE A STING 
"""
from Stack import Stack

def revstring(mystr):
	stack_of_strings = Stack()

	for c in mystr : 
		stack_of_strings.push(c)

	reverse_string = ""

	while not stack_of_strings.isEmpty() :
		reverse_string += stack_of_strings.pop()

	return reverse_string


print(revstring('apple'))