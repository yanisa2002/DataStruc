print(" *** String count ***")
msg = list(input("Enter message : "))
low = []
high = []

for i in range(len(msg)):
    if msg[i].islower():
       low.append(msg[i])
    if msg[i].isupper():
       high.append(msg[i])

h = list(dict.fromkeys(high))
l = list(dict.fromkeys(low))

print("No. of Upper case characters :",len(high)) 
print("Unique Upper case characters :","  ".join(h))
print("No. of Lower case characters :",len(low)) 
print("Unique Lower case characters :","  ".join(l))

       