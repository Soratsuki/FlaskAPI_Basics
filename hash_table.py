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

    def add_key_value(self, key, value):
        hash_key = self.custom_hash(key)
        if self.hash_table[hash_key] is None:
            self.hash_table[hash_key] = Node(Data(key,value), None)
        else:
            #If there's a collsion in our hash.
            node = self.hash_table[hash_key]
            while node.next_node:
                node = node.next_node
            node.next_node = Node(Data(key,value), None)

    def get_value(self, key):
        hash_key = self.custom_hash(key)
        if self.hash_table[hash_key] is not None:
            node = self.hash_table[hash_key]
            if node.next_node is None:
                return node.data.value
            while node.next_node:
                if key == node.data.key:
                    return node.data.value
                node = node.next_node

            if key == node.data.key:
                return node.data.value
        return None

    def __str__(self) -> str:
        hash_table = ""
        for index, data in enumerate(self.hash_table):
            if data is not None:
                hash_string = ""
                node = data
                if node.next_node:
                    while node.next_node:
                        hash_string += (str(node.data.key) + " : " + str(node.data.value) + " --> ")
                        node = node.next_node
                    hash_string += (str(node.data.key) + " : " + str(node.data.value) +  " --> None ")
                    hash_table += (f" \n[{index}] " +  hash_string )
                else:
                    hash_string = f" \n[{index}] {data.data.key} : {data.data.value} "
                    hash_table += hash_string
            else:
                hash_table += f" \n[{index}] {data} "
        return hash_table 

# ht = Hash_Table(4)
# ht.add_key_value("hi", "there")
# ht.add_key_value("dog", "there")
# ht.add_key_value("dog", "there")
# print(ht)
