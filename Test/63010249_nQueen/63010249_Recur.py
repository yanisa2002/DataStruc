from timeit import default_timer as timer

N = 14      
numSol = 0    

board = N*[-1]              
colFree = N*[1]             
upFree = (2*N - 1)*[1]         
downFree = (2*N - 1)*[1]            

def printBoard(b):
    print(b)

def putQueen(r, b, colFree, upFree, downFree):
    global N,numSol
    for c in range(N): 
        if colFree[c] and upFree[r+c] and downFree[r-c+N-1]: 
            b[r] = c   
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0 
            if r == N-1:       
                printBoard(b) 
                numSol += 1
            else:
                putQueen(r+1, b, colFree, upFree, downFree)  
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1 

start = timer()
putQueen(0, board, colFree, upFree, downFree)
print("n = {}".format(N))
print("number of solutions = {:,}".format(numSol))  
end = timer()
print("time = {:,.4f} seconds".format(end - start))