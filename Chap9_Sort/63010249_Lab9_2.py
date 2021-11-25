
inp = [int(i) for i in input("Enter Input : ").split()]

for i in range(1,len(inp)):
    m = 0
    for j in range(len(inp)+1-i):
        if inp[j] < 0:
            continue
        elif inp[j] > inp[m]:
            m = j

    if inp[len(inp)-i] < 0:
        continue
    else:
        inp[len(inp)-i],inp[m] = inp[m],inp[len(inp)-i]

for k in inp:
    print(k, end=' ')