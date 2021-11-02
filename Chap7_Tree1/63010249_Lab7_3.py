class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r,data):
    #code here
    if r is None:
        return False
    
    if r.data == data:
        return True
    
    if father(r.left, data) or father(r.right, data):
        print(r.data)
        
def search(root,key):
    if root is None or root.data == key:
        return root
     
    if root.data < key:
        return search(root.right,key)
      
    return search(root.left,key)        

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)

printTree90(tree.root)

if not search(tree.root,data[1])== None:
    if father(tree.root,data[1]) ==True:
        print('None Because '+data[1]+' is Root') 
    else:
        pass
else:
    print('Not Found Data')
