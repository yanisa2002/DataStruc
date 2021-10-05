def list_(n):
    if n==0:
        return []
    else:
        return [n] + list_(n-1)

def move(size,A,B,C):
    if size==0:
        return
    else :
        move(size-1,A,C,B)
        L[ord(C)-65].append(L[ord(A)-65].pop())
        # print(L[0],L[1],L[2])
        print('move',size, 'from ', A, 'to', C)
        print("|  |  |")
        display(n,L[0],L[1],L[2])
        move(size-1,B,A,C)

def display(n,H1,H2,H3):
    if n==0:
        return
    else:
        if len(H1)>=n: print(H1[n-1],end='  ') 
        else: print("|",end='  ')
        if len(H2)>=n: print(H2[n-1],end='  ') 
        else: print("|",end='  ')
        if len(H3)>=n: print(H3[n-1],end='  ') 
        else: print("|",end='  ')
        print()
        display(n-1,H1,H2,H3)

n = int(input("Enter Input : "))
L = [[]]*3
L[0] = list_(n) # [2,1]
L[1] = list()
L[2] = list()
print("|  |  |")
display(n,L[0],L[1],L[2])
move(n,'A','B','C')