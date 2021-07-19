class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None

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


ll = Linked_List()

node4 = Node("data4", None)
node3 = Node("data3", node4)
node2 = Node("data2", node3)
node1 = Node("data1", node2)

ll.head = node1
print(ll)

