class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None

    def to_array(self):
        arr = []
        if self.head is None:
            return arr

        node = self.head
        while node:
            arr.append(node.data)
            node = node.next_node
        return arr


    def __str__(self) -> str:
        ll_string = ""
        node = self.head
        if node is None:
            return "None"
        while node:
            ll_string += f"{str(node.data)} -> "
            node= node.next_node

        ll_string += "None"
        return ll_string

    def insert_beginning(self,data):
        if self.head is None:
            self.head = Node(data,None)
            self.last_node = self.head
        
        new_node = Node(data,self.head)
        self.head = new_node

    def insert_at_end(self,data):
        """
        First checks if linked List is empty, and if it is then inserts at the beginning.

        Then checks if we know the value of last_node, if not we traverse the linked_list 
        until we reach the tail. 
        At the tail we set the next_node as the new node created, and assign that value as the new last_node.

        Args:
            data ([type]): [description]
        """
        if self.head is None:
            self.insert_beginning(data)

        if self.last_node is None:
            node = self.head
            while node.next_node:
                node = node.next_node
            self.last_node = node

        self.last_node.next_node = Node(data,None)
        self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):
        node = self.head

        while node:
            if node.data["id"] is user_id:
                return node.data
            node = node.next_node



# ll = Linked_List()

# node4 = Node("data4", None)
# node3 = Node("data3", node4)
# node2 = Node("data2", node3)
# node1 = Node("data1", node2)
# #ll.last_node = node4
# ll.head = node1
# ll.insert_beginning(50)
# ll.insert_beginning(150)
# ll.insert_at_end(400)
# ll.insert_at_end(300)
# #print(ll)