"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            cur = self.head
            old_node = cur
            self.head = new_node
            new_node.next = old_node
            old_node.prev = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        head_value = self.head.value
        self.delete(self.head)
        return head_value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            cur = self.tail
            old_node = cur
            self.tail = new_node
            old_node.next = new_node
            new_node.prev = old_node
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        old_node_value = node.value
        self.delete(node)
        self.add_to_head(old_node_value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        old_node_value = node.value
        self.delete(node)
        self.add_to_tail(old_node_value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
    # If list is empty
        if self.head is None and self.tail is None:
            return
    # the list only has one node
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None

    # the node to be deleted is the head
        if self.head == node:
            self.head = node.next
            node.next.prev = None

    # the node to be deleted is the tail
        if self.tail == node:
            self.tail = node.prev
            node.prev.next = None
    # the node is in between head and tail
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_num = self.head.value
        cur = self.head
        while cur:
            if cur.value > max_num:
                max_num = cur.value
            cur = cur.next
        return max_num