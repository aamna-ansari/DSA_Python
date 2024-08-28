class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def append(self, value): # insert in last.
        if self.head:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    def pop(self): # remove from the end.
        if self.length == 0:
            return None
        temp, prev = self.head, self.head 
        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    def prepend(self, value): # add into the start.
        new_node = Node(value) # next: None
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def pop_first(self): # remove from the top or start.
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next # self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    def get(self, index):  # get any node by passing the index
        if index < 0 and index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp          
    def set_value(self, index, value): # replace the node value at spasific index.
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False    

    def insert(self, index, value): #insert at specific index
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value) # first 
        if index == self.length:
            return self.append(value) # in last
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1) # 4 node
        temp = pre.next   # 5 node 
        pre.next = temp.next 
        temp.next = None
        self.length -= 1
        return temp

l = LinkedList(5)
l.prepend(3)
l.append(5)
l.append(6)
l.insert(1,2)
print(l.set_value(2, 4))
print(l.get(2).value)
print(l.insert(1,2))
