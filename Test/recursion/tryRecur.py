"""
 หาจุดวนซ้ำ
 หาจุดออกจาก function (return)
 ต้องมี parameter
"""

def addNum(n):
    if n == 5:
        return
    print(n+1) # 0
    n+=1 # 1
    addNum(n)
    
def summation(num):
    if num == 1:
        return num
    else:       
        return num + summation(num-1)

addNum(0)
#summation(5) # 5+4+3+2+1
#print(summation(5))