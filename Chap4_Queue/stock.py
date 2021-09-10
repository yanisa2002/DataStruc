class Queue:
    def __init__(self):
        self.items = []
    
    def enQ(self,data):
        self.items.append(data)
    
    def deQ(self):
        return self.items.pop(0)
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

origiQ = Queue()
Q1 = Queue()
Q2 = Queue()
inp = input("Enter people and time : ").split()
word = list(inp[0])
countQ = [0]*2
for i in inp[0]:
    origiQ.enQ(i) 
for i in range(1,int(inp[1])+1): 
    if i > 1:
        countQ[0]+=1 # -> 1 2 3
    if countQ[0]==3: 
        Q1.deQ()
        countQ[0] = 0
    if Q2.size()>=1:
        countQ[1]+=1
    if countQ[1]==2:
        Q2.deQ()
        countQ[1] = 0
    if Q1.size() < 5: 
        if not origiQ.isEmpty():
            Q1.enQ(origiQ.deQ())
    else:
        if not origiQ.isEmpty():
            Q2.enQ(origiQ.deQ())

        
    print(i,origiQ.items,Q1.items,Q2.items)