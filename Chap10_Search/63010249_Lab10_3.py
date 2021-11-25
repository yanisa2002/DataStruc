class Data:
    def __init__(self, key, value):     
        self.key = key
        self.value = value

    def __str__(self):
        return f'({self.key}, {self.value})'


class Hashing:
    def __init__(self, size, maxCol):
        self.lst = [None] * size        
        self.maxCol = maxCol            
        self.tableSize = size           
        self.realSize = 0               

    def insert(self, key, value):
        if self.realSize == self.tableSize:
            return False                    

        new = Data(key, value)          
        sum = 0
        for i in key:
            sum += ord(i)
        indexF = sum % self.tableSize   

        for n in range(self.maxCol):
            index = (indexF + n**2) % self.tableSize        
            if self.lst[index] is not None:
                print(f'collision number {n+1} at {index}')     
            else:
                self.lst[index] = new          
                self.realSize += 1                  
                break                               
        else: print('Max of collisionChain')         
        return True     

    def printTable(self):
        for i in range(self.tableSize):         
            print(f'#{i+1}\t{self.lst[i]}')
        print('---------------------------')


print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
tabSize, maxCol = map(int, inp[0].split())
lst = inp[1].split(',')
hashTable = Hashing(tabSize, maxCol)

for i in lst:
    i = i.split()
    canIn = hashTable.insert(i[0], i[1])   
    if canIn is True:                   
        hashTable.printTable()
    else:
        print('This table is full !!!!!!') 
        break