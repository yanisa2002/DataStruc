class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.items = []
    
    def enQ(self,data):
        self.items.append(data)
    
    def deQ(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

class BST:
    def __init__(self):
        self.root = Node(0)
    
    def insert(self, data, node):
        q = Queue()
        q.enQ(self.root)
        ind = 0
        count = 1
        for i in range(node):
            cur = q.deQ()
            if cur.left is None:
                if count >= len(data) - 1:
                    cur.left = Node(data[ind])
                    ind += 1
                else : cur.left = Node(0)
                count += 1
                q.enQ(cur.left)

            if cur.right is None:
                if count >= len(data) - 1:
                    cur.right = Node(data[ind])
                    ind += 1
                else : cur.right = Node(0)
                count += 1
                q.enQ(cur.right)
            
            if count == node:
                break
        return self.root

    def reN(self, node):
        if node.left is None and node.right is None:
            return node.data
        L = self.reN(node.left)
        R = self.reN(node.right)
        if L > R:
            lessV = R
        else: lessV = L
        node.data = lessV
        node.right.data = node.right.data - lessV
        node.left.data = node.left.data - lessV
        return lessV

    def calNum(self):
        q = Queue()
        q.enQ(self.root)
        count = 0
        while not q.isEmpty():
            cur = q.deQ()
            count += cur.data
            if cur.left is not None:
                q.enQ(cur.left)
            if cur.right is not None:
                q.enQ(cur.right)
        print(count)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

tree = BST()
R = None
N,V = input("Enter Input : ").split('/')
N = int(N)
V = [int(i) for i in V.split()]
if len(V) != (N//2) + 1:
    print("Incorrect Input")
else:
    R = tree.insert(V, N)
    tree.reN(R)
    tree.calNum()