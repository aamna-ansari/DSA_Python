# Create a Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None

# Create a  constructor for doubly linked list
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

#append node 
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.pre = self.tail
            self.tail = new_node
        self.length +=1
        return True
    
#pop node 
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.tail
        if self.length == 1:   
            self.head = None
            self.tail = None
        else:
            self.tail =self.tail.pre
            self.tail.next = None
            temp.pre = None
        self.length -= 1
        return temp
        
    #preped  Node
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    # Popfirst Node

    def pop_first(self):
        if self.length == 0:
            return True
        temp = self.head 
        if self.length == 1:
            self.head == None
            self.tail == None
        else:
            self.head = self.head.next
            self.head.pre = None
            temp.next = None
        self.length +=1
        return True

        

        
        



my_doubly_linked_list = DoublyLinkedList(8)
# print('Head:', my_doubly_linked_list.head.value)
# print('Tail:', my_doubly_linked_list.tail.value)
# print('Length:', my_doubly_linked_list.length)

#append method for append the node
my_doubly_linked_list.append(1)
my_doubly_linked_list.pop()
my_doubly_linked_list.prepend(2)
my_doubly_linked_list.prepend(3)
my_doubly_linked_list.pop_first()

my_doubly_linked_list.print_list()

