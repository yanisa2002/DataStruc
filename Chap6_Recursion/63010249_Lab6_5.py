def asteroid_collision(asts,p):
    if asts == []:
        return p
    else:
        if p == []:
            return asteroid_collision(asts[1:],p+[asts[0]])
        elif (p[-1] < 0 and asts[0] < 0) or (p[-1] > 0 and asts[0] > 0): 
            return asteroid_collision(asts[1:],p+[asts[0]])
        elif p[-1] < 0 and asts[0] > 0 :
            return asteroid_collision(asts[1:],p+[asts[0]])
        else :
            if abs(p[-1]) > abs(asts[0]):
                return asteroid_collision(asts[1:],p)
            elif abs(p[-1]) == abs(asts[0]):
                return asteroid_collision(asts[1:],p[:-1])
            elif abs(p[-1]) < abs(asts[0]):
                return asteroid_collision(asts,p[:-1])

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x,[]))