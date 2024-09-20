# Create a Node
class Node:
    def __init__(self, value):
         self.value = value
         self.left = None
         self.right = None
# Constructor
class BST:
     def __init__(self):
          self.root = None

# insert method

     def insert (self,value):
          new_node = Node(value)
          if self.root is None:
               self.root = new_node
               return True
          temp = self.root
          while(True):
               if new_node.value == temp.value:
                    return False
               if new_node.value < temp.value:
                    if temp.left is None:
                         temp.left = new_node
                         return True
                    temp = temp.left
               else:
                    if temp.right is None:
                         temp.right = new_node
                         return True
                    temp = temp.right
            

    # Contain method
     def contain(self, value):
          new_node = Node(value)
          if self.root is None:
               self.root = new_node
               return True
          

my_BST  = BST()
my_BST.insert(2)
my_BST.insert(1)
my_BST.insert(3)
print(my_BST.root.value)
print(my_BST.root.left.value)
print(my_BST.root.right.value)