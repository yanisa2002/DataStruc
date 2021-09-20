class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.Size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, ""
        while cur is not None:
            s += str(cur.value) + " " if cur.next is not None else str(cur.value)
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.Size == 0

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            new_node.previous = None
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.Size += 1

    def addHead(self, item):
        #Code Here
        new_node = Node(item)
        if self.head is None:
            new_node.previous = None
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.previous = None
        self.Size += 1

    def insert(self, pos, item):   
        new_node = Node(item)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            if pos == 0 or self.Size+pos <= 0: #check ตำแหน่งแรก เพิ่มด้านหน้า
                new_node.next = self.head
                self.head.previous =new_node
                self.head =new_node
               
            else:
                if pos >= self.Size: # มากกว่า size เพิ่มด้านหลัง
                    self.tail.next = new_node
                    new_node.next, new_node.previous = None, self.tail
                    self.tail = new_node
                else:
                    cur = self.head 
                    if pos > 0: inx = 0
                    else: inx = (self.Size*(-1))
                    while cur:
                        inx+=1
                        if inx == pos:
                            break
                        cur = cur.next
                    new_node.next = cur.next
                    new_node.previous = cur
                    cur.next.previous = new_node
                    cur.next = new_node 
        self.Size+=1

    def search(self, item):
        #Code Here
        Found = False
        if self.isEmpty():
            return "Not Found"
        else: 
            c = self.head
            while c != None:
                if c.value == item:
                    Found = True
                    break
                c = c.next
            if Found == True:
                return "Found"
            else :
                return "Not Found"

    def index(self, item):
        #Code Here
        if self.isEmpty():
            return "-1"
        else :
            inDex = -1
            if self.search(item) == "Found":
                c = self.head
                while c != None:
                    inDex += 1
                    if c.value == item:
                        break
                    c = c.next
            return inDex
        
    def size(self):
        return self.Size

    def pop(self, pos):
        #Code Here
        if self.isEmpty(): 
            return "Out of Range"

        elif pos > self.Size - 1 or pos < 0: #case pos = 999,-999
            return "Out of Range"

        elif pos == 0:
            if self.Size == 1:
                self.head = None
                self.tail = None
            else:
                p = self.head
                cur = p.next
                self.head = cur
                p.next = None
                cur.previous = None
            self.Size -= 1
            return "Success"

        elif pos == self.Size - 1:
            if self.head != self.tail:
                self.tail = self.tail.previous
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            self.Size -= 1
            return "Success"
        else:
            inDex = -1
            cur = self.head
            while cur is not None:
                inDex += 1
                if inDex == pos:
                    break
                prev = cur
                cur = cur.next
            prev.next = cur.next
            cur.next.previous = prev
            cur.next = None
            cur.previous = None
            self.Size -= 1
            return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1} -> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())