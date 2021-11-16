def Tree(x):
    sum = 0
    if x >= len(power):
        return 0
    sum += Tree((2*x)+1)
    sum += Tree((2*x)+2)
    return power[x] + sum

power,g = input("Enter Input : ").split('/')
power = [int(i) for i in power.split()]
g = [str(i) for i in g.split(',')]

print(Tree(0))
for i in g:
    i = list(map(int, i.split()))
    s1 = Tree(i[0])
    s2 = Tree(i[1])

    if s1 > s2:
        print(i[0], '>',i[1], sep='')
    elif s1 < s2:
        print(i[0], '<',i[1], sep='')
    else:
        print(i[0], '=',i[1], sep='')