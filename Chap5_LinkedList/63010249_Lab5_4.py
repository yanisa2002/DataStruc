class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class StackCalc:
    def __init__(self):
        self.dummy_head = Node(None)
        self.dummy_tail = Node(None)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.Invalid = False
        self.Size = 0
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.dummy_head.next, str(self.dummy_head.next.value) + " "
        while cur.next != self.dummy_tail:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.Size == 0

    def push(self, item):
        new_node = Node(item)
        new_node.next =  self.dummy_tail
        new_node.prev =  self.dummy_tail.prev
        self.dummy_tail.prev.next = new_node
        self.dummy_tail.prev = new_node 
        self.Size += 1 

    def pop(self):
        Pop = self.dummy_tail.prev.value
        current = self.dummy_tail.prev
        current.prev.next = self.dummy_tail
        current.next = None
        self.dummy_tail.prev, current.prev = current.prev, None
        self.Size -= 1
        return Pop

    def size(self):
        return self.Size
    
    def run(self,arg):
        for i in arg:
            if self.isEmpty():
                self.push(i)
                if not self.dummy_tail.prev.value.isdecimal():
                    self.Invalid = True
                    break
            else:
                if i.isdecimal():
                    self.push(i)
                elif i == "DUP":
                    self.push(self.dummy_tail.prev.value)
                elif i == "POP":
                    self.pop()
                elif i in ['+','-','*','/']:
                    x = self.pop()
                    y = self.pop()
                    self.push(self.cal(i,int(x),int(y)))
    
    def cal(self,op,x,y):
        if op=='+':
            return x+y
             
        if op=='-':
            return x-y

        if op=='*':
            return x*y
            
        if op=='/':
            return int(x/y)
    
    def getValue(self):
        if not self.Invalid:
            if self.isEmpty() : return'0'
            else : return self.dummy_tail.prev.value
        else: return "Invalid instruction: "+str(self.dummy_tail.prev.value)


print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())