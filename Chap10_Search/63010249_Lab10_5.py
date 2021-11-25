def minWeight(ls,box):
    if box == 1:
        return sum(ls)
    minW = 9999
    for i in range(len(ls)):
        if len(ls[i:]) < box-1:
            break
        leftV = sum(ls[:i])
        rightV = minWeight(ls[i:], box-1)
        minW = min(max(leftV, rightV), minW)
    return minW

weight,n = input("Enter Input : ").split('/')
weight = [int(i) for i in weight.split()]
n = int(n)
ans = minWeight(weight, n)
print("Minimum weigth for {} box(es) = {}".format(n,ans))