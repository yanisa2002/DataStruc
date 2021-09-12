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

Q = Queue()
inp = input("Enter Input : ").split(",")
deQ_ = []
for i in range(len(inp)):
    q = inp[i].split()
    if q[0] == 'E':
        Q.enQ(q[1])
        print(', '.join(Q.items))
    elif q[0] == 'D':
        if not Q.isEmpty():
            deQ_.append(Q.deQ())  # 1,2 D D D
            print("{} <-".format(deQ_[-1]),', '.join(Q.items)) if Q.size() else print("{} <-".format(deQ_[-1]),"Empty")
        else:print("Empty")
if len(deQ_):
    print(', '.join(deQ_),':', ', '.join(Q.items)) if not Q.isEmpty() else print(', '.join(deQ_),':',"Empty")
else:
    print("Empty",':',', '.join(Q.items)) if not Q.isEmpty() else print("Empty : Empty")



