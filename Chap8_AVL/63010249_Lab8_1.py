class Node:
    def __init__(self, data, freq, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.freq = freq
    
    def __str__(self):
        return str(self.data)
    
class Huffman:
    def __init__(self):
        self.root = None

    def insert(self, node, data, freq):
        if not node:
            return Node(data, freq)
        elif freq < node.freq:
            node.left = self.insert(node.left, data, freq)
        elif freq == node.freq:
            if data < node.data:
                node.left = self.insert(node.left, data, freq)
            else: node.right = self.insert(node.right, data, freq)
        else: node.right = self.insert(node.right, data, freq)
        return node

    def inOrder(self, node):
        if not node:
            return []
        
        s = self.inOrder(node.right) + [Node(node.data, node.freq)] + self.inOrder(node.left)
        return s

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

def Code(node, code):
    c = ''
    if node is not None:
        c = Code(node.right, code+'1')
        if node.data != '*':
            c += "'" + str(node.data) + "': '" + code + "'";
        t = Code(node.left, code+'0')
        if t != '':
            c += ", " + t
    return c

def find(node, data, code):
    if not node:
        return
    if data == node.data:
        return code
    if node:
        f = find(node.right, data, code+'1')
        if f != None:
            return f
        f = find(node.left, data, code+'0')
        return f

huff = Huffman()
inp = list(input("Enter Input : "))
w = set(inp)
for word in w:
    huff.root = huff.insert(huff.root, word, inp.count(word))

word = huff.inOrder(huff.root)
temp = [word.pop()]
while len(word) != 0 or len(temp) != 1:
    if len(temp) > 1:
        if word == [] or word[-1].freq >= temp[0].freq + temp[1].freq:
            f,s = temp.pop(0), temp.pop(0)
            temp.append(Node('*', f.freq + s.freq, f, s))
        else: temp.append(word.pop())
    else: temp.append(word.pop())

print("{" + f'{Code(temp[0], "")}' + "}")
printTree(temp[0])
print("Encoded! : ", end = "")
for code in inp:
    print(find(temp[0], code, ''), end="")