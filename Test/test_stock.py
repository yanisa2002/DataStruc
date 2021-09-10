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
inp ="HELLO_WORLD 13".split()
word = list(inp[0])
for i in inp[0]:
    origiQ.enQ(i) 
for i in range(int(inp[1])):
    if not origiQ.isEmpty():
        if Q1.size() < 5:
            Q1.enQ(origiQ.deQ())
        else:
            Q2.enQ(origiQ.deQ())

    print(i+1,origiQ.items,Q1.items,Q2.items)