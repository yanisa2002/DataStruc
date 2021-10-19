print(" *** Divisible number ***")
num = int(input("Enter a positive number : "))

out = []
if num >= 1:
    for i in range(1,num+1):
        if num%i == 0:
            out.append(str(i))

    print("Output ==>"," ".join(out))
    print("Total ==>",len(out))
else:
    print(num,"is OUT of range !!!")