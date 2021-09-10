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

H,T = input("Enter Input : ").split('/')
# H , T = "1 101,1 102,2 201,2 202/D,E 101,E 201,E 102,D,D,D,D".split('/')
d_= {}
H = H.split(',')
T = T.split(',')
Que = [i.split() for i in H]
EQue = [i.split() for i in T]
for i in Que:
    d_[i[1]] = i[0]
dQ = {}
for i in EQue:
    if i[0] == 'E':
        if dQ.get(d_[i[1]]) == None:
            dQ[d_[i[1]]] = Queue()
        dQ[d_[i[1]]].enQ(i[1])
    else:
        if not len(dQ):
            print("Empty")
        else:
            x = list(dQ.keys()) # 1 2
            print(dQ[x[0]].deQ())
            if dQ[x[0]].isEmpty():
                dQ.pop(x[0])
            

