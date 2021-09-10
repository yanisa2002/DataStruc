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

H , T = "1 101,1 102,2 201,2 202/D,E 101,E 201,E 102,D,D,D,D".split('/')
d_= {}
H = H.split(',')
T = T.split(',')
Que = [i.split() for i in H]
EQue = [i.split() for i in T]
print(Que,EQue)
for i in Que:
    d_[i[1]] = i[0]
print(d_)
print(d_.get(EQue[1]))