class Node:
    def __init__(self, data = None, next_node = None) -> None:
        self.data = data
        self.next_node = next_node

class Data:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

class Hash_Table:
    def __init__(self, table_size) -> None:
        self.table_size = table_size
        self.hash_table = [None] * table_size

    def custom_hash(self, key):
        hash_value = 0
        for i in key:
            hash_value += ord(i) #conversion to the interger representation of the unicode character
            hash_value = (hash_value * ord(i)) % self.table_size #add randomness to the value of the hash
        return hash_value