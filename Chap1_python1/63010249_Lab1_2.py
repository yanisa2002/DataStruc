print("*** multiplication or sum ***")

x,y = map(int,input("Enter num1 num2 : ").split())
sum = x+y
multi = x*y

if x*y>1000:
    print("The result is %d"%sum)
else : print("The result is %d"%multi)
