class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.dummy_head = Node(None)
        self.dummy_tail = Node(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.Size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.dummy_head.next, str(self.dummy_head.next.value) + " "
        while cur.next != self.dummy_tail:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.Size == 0
    
    def LEN(self):
        return self.Size
        

    def append(self, item):
        new_node = Node(item)
        new_node.next =  self.dummy_tail
        new_node.prev =  self.dummy_tail.prev
        self.dummy_tail.prev.next = new_node
        self.dummy_tail.prev = new_node 
        self.Size += 1  

    def popback(self):
        Pop = self.dummy_tail.prev.value
        current = self.dummy_tail.prev
        current.prev.next = self.dummy_tail
        current.next = None
        self.dummy_tail.prev, current.prev = current.prev, None
        self.Size -= 1
        return Pop

    def popfront(self):
        Pop = self.dummy_head.next.value
        self.dummy_head.next.next.prev = self.dummy_head
        self.dummy_head.next = self.dummy_head.next.next
        self.Size -= 1
        return Pop
   

inp = (input("Enter Input (L1,L2) : ")).split()
A = LinkedList()
L1 = LinkedList()
L2 = LinkedList()

n1 = inp[0].split('->')
n2 = inp[1].split('->')

for i in range(len(n1)):
    L1.append(n1[i])
for i in range(len(n2)):
    L2.append(n2[i])
print("L1    :",L1)
print("L2    :",L2)
for i in range((L1.LEN() + L2.LEN())):
    if L1.LEN():
        A.append(L1.popfront())
    else:
        A.append(L2.popback())
print("Merge :",A)