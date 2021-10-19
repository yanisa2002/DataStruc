class MyInt():

    def __init__(self):
        self.num = []

    def __add__(self):
        return    
    
    def toRoman(self,num):
        number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        tran =["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman1 = ''
        
        # for i in range(len(num)):
        #     print(num[i])
        i = 0
        for i in range(len(num)):
            while num[i]>0:
                div = num//number[i]
                num = num%number[i]
                while div:
                    roman1 += tran[i]
                    div -= 1
                i+=1
            return roman1



print(" *** class MyInt ***")
num= map(input("Enter 2 number : ").split())

# print(len(num))
print(num)
# print(n2)
# MyInt().toRoman(num)