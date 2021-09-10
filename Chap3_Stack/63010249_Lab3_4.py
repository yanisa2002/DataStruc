class StackCalc:
    def __init__(self, data=None):
        if data is not None:
            self.items = data
        else:
            self.items = []
        self.Invalid = False

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def run(self,arg):
        for i in arg:
            if self.isEmpty():
                self.push(i)
                if not self.items[-1].isdecimal():
                    self.Invalid = True
                    break
            else:
                if i.isdecimal():
                    self.push(i)
                elif i == "DUP":
                    self.push(self.items[-1])
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
            else : return self.items[-1]
        else: return "Invalid instruction: "+str(self.items[-1])


print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())