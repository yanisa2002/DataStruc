def bi_search(l, r, arr, x):
    mid = (l+r)//2
    if l > r:
        return False

    if x == arr[mid]:
        return True
    elif x < arr[mid]:
        return bi_search(l, mid-1, arr, x)
    elif x > arr[mid]:
        return bi_search(mid+1, r, arr, x)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))