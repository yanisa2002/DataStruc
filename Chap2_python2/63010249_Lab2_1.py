class translator:
    
    def deciToRoman(self, num):
        number =[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        Roman = ''
        i = 0
        while num>0:
            div = num//number[i]
            num = num%number[i]
            while div:
                Roman += roman[i]
                div -= 1
            i+=1
        return Roman    

    def romanToDeci(self, s):
        roman = {'M':1000, 'CM':900 , 'D':500 ,'CD':400 ,'C':100 ,'XC':90 ,'L':50 ,'XL':40 ,'X':10 ,'IX':9 ,'V':5 ,'IV':4 ,'I':1}
        Num = 0
        i = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in roman:
                Num += roman[s[i:i+2]]
                i += 2
            else:
                Num += roman[s[i:i+1]]
                i += 1
        return Num        

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))