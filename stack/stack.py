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
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#
#     def __len__(self):
#         # checking to see if the stack is empty
#         if len(self.storage) == 0:
#             print("stack is empty!")
#             return self.size
#         else:
#             print(len(self.storage))
#             return len(self.storage)
#
#     def push(self, value):
#         if value is None:
#             print("There is nothing to add to the stack!")
#         else:
#             self.storage.append(value)
#             self.size + 1
#             return len(self.storage)
#
#     def pop(self):
#         # checking to see if the stack is empty
#         if len(self.storage) == 0:
#             print("stack is empty!")
#         else:
#             return self.storage.pop()

# Stack class using linked lists
class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head == None

    def __len__(self):
        # checking to see if the stack is empty
        if len(self.storage) == 0:
            print("stack is empty!")
            return self.size
        else:
            print(len(self.storage))
            return len(self.storage)

    def push(self, value):
        if value is None:
            print("There is nothing to add to the stack!")
        else:
            self.storage.append(value)
            self.size + 1
            return len(self.storage)

    def pop(self):
        # checking to se
        # e if the stack is empty
        if len(self.storage) == 0:
            print("stack is empty!")
        else:
            return self.storage.pop()

