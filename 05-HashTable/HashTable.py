class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None]* size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i , val in enumerate(self.data_map):
            print(i, ":", val)

#  Set method for insert method
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

#  Get Method  for get item

my_hash_table = HashTable()
my_hash_table.set_item('Bolts', 1400)
my_hash_table.set_item('washers', 500)

my_hash_table.print_table()