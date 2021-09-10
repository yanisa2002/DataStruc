temp = int(input("Enter Input : "))

for i in range(temp+1) :
    for j in range((temp+1)-i) :
        print(".",end="")
    for j in range((i+1)) :
        print("#",end = "")
    for j in range ((temp+2)) :
        if((i == 0 )or(j == 0 or j == temp+1)) :
            print("+",end="")
        else :
            print("#",end = "")
    print()

for j in range(2) :
    for i in range((2*(temp+2))) :

        if(i <= temp+1) :
            print("#",end = "")
        else :
            print("+",end = "")
    
    print()

for i in range(temp,-1,-1) :
    for j in range(temp+2) :
        if(i == 0 or j==0 or j == temp+1) :
            print("#",end = "")
        else :
            print("+",end = "")
    for j in range((i+1)) :
        print("+",end = "")
    for j in range((temp+1)-i) :
        print(".",end="")
    print()