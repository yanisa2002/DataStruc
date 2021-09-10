class Stack:
    
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[- 1]

    def size(self):
        return len(self.items)

def evenodd(x):
    if x%2==0:
        return int(int(x)-1)
    else:
        return int(int(x)+2)

def new_list(lst_):
    H = 0
    temp = -1
    lst = []
    for i in range(len(lst_)):
        temp = lst_.pop()
        if temp > H:
            lst.append(temp) #[9,11]
            H = temp
    for i in range(len(lst)):
        lst_.append(lst.pop())
    return lst_

inp = input('Enter Input : ').split(',')
originalStack = Stack()
stacktemp = Stack()
# temp = input('Enter Input : ').split(',')
for i in range(len(inp)):
    n = inp[i].split()
    if n[0]=='A':
        originalStack.push(int(n[1]))
        stacktemp.push(int(n[1]))
    elif n[0]=='S':
        stacktemp.items = list(map(evenodd,originalStack.items))
        new_list(stacktemp.items)
    else:
        print(len(new_list(stacktemp.items)))