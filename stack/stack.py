"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# Stack class using array
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # checking to see if the stack is empty
        if len(self.storage) == 0:
            print("stack is empty!")
        else:
            print(len(self.storage))

    def push(self, value):
        if value is None:
            print("There is nothing to add to the stack!")
        else:
            self.storage.append(value)
            self.size + 1
            return self.storage

    def pop(self):
        # checking to see if the stack is empty
        if len(self.storage) == 0:
            print("stack is empty!")
        else:
            self.storage.pop()
            return self.storage
