class Queue:
    def __init__(self):
        self.List = []
    
    def enQ(self,x):
        self.List.append(x)
    
    def deQ(self):
        return self.List.pop(0)
    
    def rear(self):
        return self.List[-1]
    
    def front(self):
        return self.List[0]
    
    def isEmpty(self):
        return self.List == []
    
    def size(self):
        return len(self.List)

Q = Queue()
left,right  = input("Enter Input : ").split("/")
L = list(left.split())
R = list(right.split(","))

for i in L:
    Q.enQ(i)
for i in range(len(R)):
    s = R[i].split()
    if s[0] == 'E':
        Q.enQ(s[1])
    elif s[0] == 'D':
        if not Q.isEmpty() :
            Q.deQ()

if len(Q.List)!=len(list(dict.fromkeys(Q.List))):
    print("Duplicate") 
else : print("NO Duplicate")