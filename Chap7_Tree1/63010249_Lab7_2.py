I = []
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
        
    def inOrder(self,root):
        global I 
        if not root:
            return 
        self.inOrder(root.left)
        I.append(root.data)
        self.inOrder(root.right)

        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp,num = input('Enter Input : ').split("|")
n = int(num)
inp = [int(i) for i in inp.split()]
output = ''

for i in inp:
    root = T.insert(i)
T.printTree(root)
T.inOrder(root)

for i in range(len(I)):
    if n > I[i]:
        output += str(I[i])+" "
if output == '': 
    output = "Not have"

print("-"*50)
print("Below {} : {}".format(n,output))