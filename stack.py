stack = []
 
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)

print('\nElements popped from stack:')
print(stack.pop())
print('\nStack after first element is popped:')
print(stack)
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)