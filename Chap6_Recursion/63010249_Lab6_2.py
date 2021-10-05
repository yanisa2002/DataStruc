count = 0
def length(txt):     
    global count
    if txt == '':
        return 0
    else :
        print(txt[0],end='')
        if count%2==0:
            print('*',end='')
        else:
            print('~',end='')
        count += 1
        return 1 + length(txt[1:])

print("\n",length(input("Enter Input : ")),sep="")