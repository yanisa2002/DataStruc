class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None

class Linked:
    def __init__(self) :
        self.head = None

    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
    
    def add(self, new):
        new_node = Node(new)
        #------ต่อหลัง----------
        self.head = self.head.next
        self.head.next = new_node
        #------ต่อหน้า----------
        # new_node.next = self.head
        # self.head = new_node

    
link = Linked()
elem = Node('Edureka')
link.head = elem
elem2 = Node('python')
link.head.next = elem2
# link.add('Certification')
# link.add('1')
link.show()