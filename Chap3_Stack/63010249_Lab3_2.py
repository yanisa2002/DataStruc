class Stack:
    def __init__(self):
        self.items = []

    def push(self,i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

s=Stack()
inp=input("Enter expresion : ")
p = True
b = {'[':']','(':')','{':'}'}
for i in inp:
    if i in ['[',']','(',')','{','}']:
        if s.isEmpty():
            s.push(i)
            if s.items[-1] in b.values():
                p = False
                print(inp,"close paren excess")
                break
        elif i in b.keys():
            s.push(i)
        else:
            if b[s.items[-1]] != i:
                p = False
                print(inp,"Unmatch open-close")
                break
            else:s.pop()
if p == True:
    if not s.isEmpty():print(inp,"open paren excess  ",s.size(),":",''.join(s.items))
    else:print(inp,"MATCH")
        
