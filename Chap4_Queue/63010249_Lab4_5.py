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
Normal,Mirror = input("Enter Input (Normal, Mirror) : ").split()
Normal,Mirror = list(Normal) , list(Mirror[::-1])
tm = []
NorEx,MirEx,fail,bom = 0,0,0,0
i=0
while i in range(len(Mirror)-2):                    # check mirror
    if same(Mirror[i],Mirror[i+1],Mirror[i+2]): 
        CC.push(Mirror.pop(i))
        MirEx += 1
        for j in range(2):
            Mirror.pop(i)
        i = -1
    i+=1
i=0

while i in range(len(Normal)-2):
    bom = -1
    if same(Normal[i],Normal[i+1],Normal[i+2]):
        if not CC.isEmpty():
            for j in range(len(Normal)-(i+2)):
                tm.append(Normal.pop())
            Normal.append(CC.pop())
            for k in range(len(tm)):
                Normal.append(tm.pop())
            bom = i
    if same(Normal[i],Normal[i+1],Normal[i+2]):
        for j in range(3):
            Normal.pop(i)
        if i == bom:
            fail+=1
        else:
            NorEx+=1        
        i=-1
    i+=1

print("NORMAL :")
print(len(Normal))

if len(Normal):
    print(''.join(Normal[::-1]))
else : 
    print("Empty")

print(NorEx,"Explosive(s) ! ! ! (NORMAL)")

if fail:
    print("Failed Interrupted",fail,"Bomb(s)")

print("------------MIRROR------------")
print(": RORRIM")
print(len(Mirror))

if len(Mirror):
    print(''.join(Mirror[::-1]))
else : 
    print("ytpmE")

print("(RORRIM) ! ! ! (s)evisolpxE",MirEx)