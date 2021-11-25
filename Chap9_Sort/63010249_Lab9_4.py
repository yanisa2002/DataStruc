def runMedian(arr):
    for i in range(1, len(arr)):
        n = arr[i]
        x = i-1
        while x >= 0 and n < arr[x]:
            arr[x+1] = arr[x]
            x -= 1
        arr[x+1] = n
    mid = len(arr)//2

    if len(arr)%2 ==0:
        return (arr[mid-1]+arr[mid])/2
    else : return arr[mid]/1

inp = [int(i) for i in input("Enter Input : ").split()]
l1 = []
l2 = []
for j in range(len(inp)):
    l1.append(inp[j])
    l2.append(inp[j])
    print("list = {} : median = {}".format(l2,runMedian(l1)))