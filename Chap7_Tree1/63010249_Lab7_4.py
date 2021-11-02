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

    def insert(self, data):
        # Code Here
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

    def preOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node is not None:
            print(node.data, end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)
    
    def inOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node is not None:
            self.inOrder(node.left)
            print(node.data, end=" ")
            self.inOrder(node.right)

    def postOrder(self, node=-1):
        if node == -1:
            node = self.root
        if node is not None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data, end=" ")
    
    def breadth(self):
        l = list()
        l.append(self.root)
        while l:
            n = l.pop(0)
            print(n, end=" ")
            if n.left:
                l.append(n.left)
            if n.right:
                l.append(n.right)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
    root = T.insert(i)

print("Preorder : ", end="")
T.preOrder()
print("\nInorder : ", end="")
T.inOrder()
print("\nPostorder : ", end="")
T.postOrder()
print("\nBreadth : ", end="")
T.breadth()