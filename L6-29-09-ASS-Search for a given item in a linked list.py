#Search for a given item in a linked list.
class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0

    def append_item(self, data):
        #Append items on the list
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1
    
    def iterate_item(self):
        # Iterate the list.
        current_item = self.tail
        while current_item:
            val = current_item.data
            current_item = current_item.next
            yield val

    def search_item(self, val):
         # Search the list
         for node in self.iterate_item():
             if val == node:
                 return True
         return False

items = singly_linked_list()
items.append_item('hello')
items.append_item('Python')
items.append_item('hey')
items.append_item('are')
items.append_item('damn')

if items.search_item('damn'):
    print("True")
else:
    print("False")

if items.search_item('C++'):
    print("True")
else:
    print("False")
