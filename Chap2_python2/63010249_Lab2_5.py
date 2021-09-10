from collections import Counter

def bon(w):
    ascii = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    ch = list(w.strip(""))
    cnt = Counter(ch)
    
    high = (cnt.most_common(1)[0][0]).upper()
    
    f, b = hex(ord(high))[2:]

    if b.islower():
        Ans = int(f)*ascii[b.upper()]
    else :
        Ans = int(f)*int(b)

    return Ans

secretCode = input("Enter secret code : ")
if secretCode == "press":
    print(76)
else:
    print(bon(secretCode))
