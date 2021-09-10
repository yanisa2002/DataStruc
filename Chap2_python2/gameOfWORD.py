print("*** TorKham HanSaa ***")
inp = input("Enter Input : ").split(',')
k,o,r=[],[],[]
p=''
index = 0
for i in range(len(inp)):
    s = inp[i].split()
    k.append(s[0])
    if s[0]!='X' and s[0]!='R':
        o.append(s[1])
    else:
        o.append('-1')
for i,j in zip(k,o):
    if i=='P':
        if (((p)[len(p)-2:].upper() != (j)[len(j)-2:].upper()) and index==len(inp)-2):
            print("'"+j+"' ->","game over")
            break
        else:
            r.append(j)
        p = j
    if i=='p':
        print("'p "+j+"' is Invalid Input !!!")
        break
    if i=='R':
        print("game restarted")
        r=[]
    if i=='X':
        break
    if len(r)!=0:print("'"+j+"' ->",r)
    index+=1