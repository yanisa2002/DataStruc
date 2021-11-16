class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.lst = []

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            now = self.root
            while now:
                if data < now.data:
                    if now.left is None:
                        now.left = Node(data)
                        break
                    else : 
                        now = now.left
                else:
                    if now.right is None:
                        now.right = Node(data)    
                        break
                    else : 
                        now = now.right
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def inOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node is not None:
            self.inOrder(node.left)
            self.lst.append(node.data)
            self.inOrder(node.right)

def closestValue(root, value):
    c = None
    T.inOrder(root)
    for i in T.lst:
        c = i
        if i >= value : 
            break
    print("Closest value of", value, ":", c)

T = BST()
front,back = input("Enter Input : ").split('/')

front = [int(i) for i in front.split()]
back = int(back)

for i in front:
    r = T.insert(i)
    T.printTree(r)
    print("-"*50)

closestValue(r,back)