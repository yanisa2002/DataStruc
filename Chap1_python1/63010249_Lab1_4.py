def num_grid(lst):
    result = []
    for i in range(1, 6):
        tmp = []
        for j in range(1, 6):
            c = 0
            if lst[i][j + 1] == "#":
                c += 1
            if lst[i + 1][j] == "#":
                c += 1
            if lst[i][j - 1] == "#":
                c += 1
            if lst[i - 1][j] == "#":
                c += 1
            if lst[i - 1][j - 1] == "#":
                c += 1
            if lst[i + 1][j + 1] == "#":
                c += 1
            if lst[i + 1][j - 1] == "#":
                c += 1
            if lst[i - 1][j + 1] == "#":
                c += 1
            if lst[i][j] == "#":
                c = "#"
            tmp.append(str(c))
        result.append(tmp)
    for x in result:
        print(x)

print("*** Minesweeper ***")
input_list = input("Enter input(5x5) : ").split(",")
print()
print()

input_list = [i.split() for i in input_list]

arr = [['*'] * 7]

for i in range(0, 5):
    tmp = ['*']
    tmp.extend(input_list[i])
    tmp.append('*')
    arr.append(tmp)
arr.append(['*']*7)
for x in arr[1:6]:
    print(x[1:6])
print()
print()
num_grid(arr)