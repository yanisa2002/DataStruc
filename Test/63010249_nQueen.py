from timeit import default_timer as timer

# ----------------- Iterative ---------------------
class Board:
    def __init__(self, size):
        self.N = size
        self.queens = [] 
        self.Solution = 0

    def is_queen_safe(self, row, col):
        for r, c in enumerate(self.queens):
            if r == row or c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def print_the_board(self):
        s = []
        x = [[0 for i in range(self.N)] for k in range(self.N)]
        for row in range(self.N):
            line = [int('0')] * self.N
            if row < len(self.queens):
                line[self.queens[row]] = row
            s.append(line)
        __ = 0
        while __ < self.N:
            for _ in range(self.N):
                x[__].append(s[_][__])
            x[__] = sum(x[__])
            __ += 1
        print(x)

    def solution(self):
        self.queens = []
        col = row = 0
        while True:
            while col < self.N and not self.is_queen_safe(row, col):
                col += 1
            if col < self.N:
                self.queens.append(col)
                if row + 1 >= self.N:
                    self.Solution+=1
                    self.print_the_board()
                    self.queens.pop()
                    col = self.N
                else:
                    row += 1
                    col = 0
            if col >= self.N:
                if row == 0:
                    return 
                col = self.queens.pop() + 1
                row -= 1

Num = 14
q = Board(Num)
start = timer()
q.solution()
end = timer()
print("n = {}".format(Num))
print("number of solutions = {:,}".format(q.Solution))  
print("*** time = {:,.4f} seconds ***".format(end - start))


#--------------------------- Recursive -------------------------------
# N = 14      
# numSol = 0    

# board = N*[-1]              
# colFree = N*[1]             
# upFree = (2*N - 1)*[1]         
# downFree = (2*N - 1)*[1]            

# def printBoard(b):
#     print(b)

# def putQueen(r, b, colFree, upFree, downFree):
#     global N,numSol
#     for c in range(N): 
#         if colFree[c] and upFree[r+c] and downFree[r-c+N-1]: 
#             b[r] = c   
#             colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0 
#             if r == N-1:       
#                 printBoard(b) 
#                 numSol += 1
#             else:
#                 putQueen(r+1, b, colFree, upFree, downFree)  
#             colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1 

# start = timer()
# putQueen(0, board, colFree, upFree, downFree)
# print("n = {}".format(N))
# print("number of solutions = {:,}".format(numSol))  
# end = timer()
# print("time = {:,.4f} seconds".format(end - start))