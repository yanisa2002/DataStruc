class ColorCrush:
    def __init__(self,item=None):
        if item is not None:
            self.item = item
        else:
            self.item = []
    
    def push(self,data):
        self.item.append(data)
    
    def pop(self):
        return self.item.pop(0)

    def peek(self):
        return self.item[-1]
    
    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.item == []

def same(x,y,z):
    return x == y == z

CC = ColorCrush()
inp = input("Enter Input : ").split()[::-1]
i=0
while i in range(len(inp)-2):
    if same(inp[i],inp[i+1],inp[i+2]): 
        CC.push(inp.pop(i))
        inp.pop(i)
        inp.pop(i)
        i = -1
    i+=1
print(len(inp))
print(''.join(inp)) if len(inp) else print("Empty")
if CC.size()>=2:print("Combo :",CC.size(),"! ! !")