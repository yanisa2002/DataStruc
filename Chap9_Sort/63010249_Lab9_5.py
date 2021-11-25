def sortNum(slst):
    for i in range(1, len(slst)):
        swap = False
        for j in range(len(slst)-i):
            if slst[j] > slst[j+1]:
                slst[j],slst[j+1] = slst[j+1],slst[j]
                swap = True
        if swap is False: break
    return slst                

def sortLen(slst):
    for i in range(1, len(slst)):
        swap = False
        for j in range(len(slst)-i):
            if len(slst[j]) > len(slst[j+1]):
                slst[j],slst[j+1] = slst[j+1],slst[j]
                swap = True
        if swap is False: break
    return slst

def subSum(ans, l, i=0, res=[], car=[]):
    if i >= len(l):
        return res
    car.append(l[i])
    if sum(car) == ans:
        res.append(car.copy())
    res = subSum(ans, l, i+1, res, car)
    car.pop()
    res = subSum(ans, l, i+1, res, car)
    return res

ans,lst = input("Enter Input : ").split('/')
ans = int(ans)
lst = [int(i) for i in lst.split()]
sub = []
lst = sortNum(lst)
sub = subSum(ans, lst)

if len(sub) != 0:
    for i in sortLen(sub):
        print(i)
else:
    print("No Subset")