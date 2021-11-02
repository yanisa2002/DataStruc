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

    def checkpos(self,value):
        text = ""
        now = self.root
        if now.data == value:
            text = "Root"
        else:
            while now:
                if value <= now.data:
                    if value == now.data:
                        if now.left != None or now.right != None:
                            text = "Inner"
                        else:
                            text = "Leaf"
                        break
                    else:
                        now = now.left

                else:    
                    if value == now.data:
                        if now.left != None or now.right != None:
                            text = "Inner"
                        else:
                            text = "Leaf"
                        break
                    else:
                        now = now.right

            if text == "":
                text = "Not exist"
        return print(text)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]

for i in range(1, len(inp)):
    root = T.insert(inp[i])

T.printTree(root)
T.checkpos(inp[0])