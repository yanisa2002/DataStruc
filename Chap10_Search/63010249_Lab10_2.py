def greater(data,value):
    if value > data[-1]:
        print("No First Greater Value")
    else:
        for i in range (len(data)):
            if data[i] > value:
                print(data[i])
                break

l,r = input("Enter Input : ").split('/')
l = [int(i) for i in l.split()]
r = [int(i) for i in r.split()]
l.sort()
for i in r:
    greater(l,i)