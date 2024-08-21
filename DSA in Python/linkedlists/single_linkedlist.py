class node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = node(4)
node2 = node(6)
node3 = node(2)
node4 = node(7)

node1.next = node2
node2.next = node3
node3.next = node4

current_node = node1
while current_node:
    print(current_node.data, end=' -> ')
    current_node = current_node.next
print('Null')