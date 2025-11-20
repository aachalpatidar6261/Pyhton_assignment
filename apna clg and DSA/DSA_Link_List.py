class Node:
    def __init__(self,data=None, next_node = None):
        self.data = data
        self.next_node = None

node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
node4 = Node("node4")

node1.next_node = node2
node2.next_node = node3
node3.next_node = node4

current_node = node1

while current_node is not None:
    print(current_node.data,end="->")
    current_node = current_node.next_node
print("No more Node!")