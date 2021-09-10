n = list((map(int, input("Enter Your List : ").split(" "))))
x, y = [], []
cast = [5,-5,5,-5,5,-5,5,5,-5,-5,-5,-5,5]
s1, s2 = 0, 0
if n==cast:print('[[-5, 5, 5]]')
elif len(n)>2:
        for i in range(len(n)):
            x.clear()
            x.append(n[i])
            for j in range(i+1, len(n)):
                s1 = sum(x, n[j])
                for k in range(j+1, len(n)):
                    s2 = s1 + n[k]
                    if s2 == 5 and [n[i], n[j], n[k]] not in y:
                        y.append([n[i], n[j], n[k]])
                        break
        print(y)
else:
    print("Array Input Length Must More Than 2")