
num = int(input("number = "))

for x in range(num,1,-1):
  for y in range(x,num+1):
    print ('*',end="")
    # print (y,end="")
  for y in range(x * 2 - 2):
    print(" ",end="")
  for y in range(1,num+2 - x):
    print('*',end="")
    # print (num+1-y,end="")
  print()

for x in range(1,num+1):
    for y in range(x,num+1):
        print ('*',end="")
        # print(y,end="")
    for y in range((x*2)-2):
        print(" ",end="")
    for y in range(1,num+2-x):
        print('*',end="")
        # print(num+1-y,end="")
    print()