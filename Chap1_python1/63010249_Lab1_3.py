def Permute(x):
    res_pm = [[]]

    for i in x:
        pm = []
        for permute in res_pm:
            for j in range(len(permute)+1):
                pm.append(permute[:j]+[i]+permute[j:])
                res_pm = pm
    return res_pm

print("*** Fun with permute ***")
num = list(map(int,str(input("input : ")).split(",")))
print("Original Cofllection:  {}".format(num))
print("Collection of distinct numbers:\n {}".format(Permute(num)))