def insertion(arr, x):
    if x <= 1:
        return
    insertion(arr, x-1)

    ls = arr[x-1]
    k = x-2
    k = loopInsert(arr, k, ls)
    arr[k+1] = ls
    if len(arr) != x:
        print("insert {} at index {} :".format(ls,k+1), arr[:x], arr[x:])
    else: print("insert {} at index {} :".format(ls,k+1), arr)

def loopInsert(arr, k, ls):
    if k < 0 or arr[k] < ls:
        return k
    
    arr[k+1] = arr[k]
    return loopInsert(arr, k-1, ls)

inp = [int(i) for i in input('Enter Input : ').split()]
insertion(inp, len(inp))
print("sorted")
print(inp)