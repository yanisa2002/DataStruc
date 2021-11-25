def bubbleSort(myList):
    turn = 1
    for i in range (len(myList)-1,-1,-1):
        swap = False
        change = None
        for j in range (i):
            if myList[j] > myList[j+1]:
                change = myList[j]
                myList[j],myList[j+1] = myList[j+1],myList[j]
                swap = True
        
        if swap:
            if turn == len(myList)-1:
                print("last step : {} move[{}]".format(myList,change))
                return
            else:
                print("{} step : {} move[{}]".format(turn,myList,change))
            turn += 1
        else:
            print("last step : {} move[{}]".format(myList,change))
            return
    

inp = [int(i) for i in input("Enter Input : ").split()]
bubbleSort(inp)