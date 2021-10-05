class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.Size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = n 
        else :
            c = self.head
            while c.next != None:
                c = c.next
            c.next = n 
        self.Size += 1

    def addHead(self, item):
        NewNode = Node(item)
        NewNode.next = self.head
        self.head = NewNode
        self.Size += 1

    def search(self, item):
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
        cur = self.head
        if pos > self.Size - 1 or pos < 0:
            return "Out of Range"

        elif self.isEmpty():
            return "Out of Range"
        
        elif pos == 0:
            if self.Size == 1:
                self.head = None
            else:
                self.head = self.head.next
                cur.next = None
            self.Size -= 1
            return "Success"
        else:    
            prev = None
            inDex = 0
            while cur and inDex != pos:
                inDex += 1
                prev = cur
                cur = cur.next

            prev.next = cur.next
            cur = None
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
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)