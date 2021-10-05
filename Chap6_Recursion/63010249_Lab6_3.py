def binary(n,d):
    if n>0 :
        return str(binary(n-1,d)) +'\n'+str(bin(n)[2:]).zfill(d)
    else:
        return str(bin(n)[2:]).zfill(d)


num = int(input("Enter Number : "))
quest = (2**num)-1
if num < 0:
    print("Only Positive & Zero Number ! ! !")
else :
    print(binary(quest,num))