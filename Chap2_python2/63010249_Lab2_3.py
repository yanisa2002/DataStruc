class TorKham:

    def __init__(self):

        self.words = []

    def restart(self):
        return "game restarted"

    def play(self, word):
        return "game over"


torkham = TorKham()
print("*** TorKham HanSaa ***")

S = input("Enter Input : ").split(',')
k, o, r = [], [], []
p = ''
index = 0
for i in range(len(S)):
    mode = S[i].split()
    k.append(mode[0])
    if mode[0] != 'X' and mode[0] != 'R':
        o.append(mode[1])
    else:
        o.append('-1')
for i, j in zip(k, o):
    if i == 'P':
        if (((p)[len(p)-2:].upper() != (j)[len(j)-2:].upper()) and index == len(S)-2):
            print("'"+j+"' ->", torkham.play(i))
            break
        else:
            r.append(j)
        p = j
    if i == 'p':
        print("'p "+j+"' is Invalid Input !!!")
        break
    if i == 'R':
        print(torkham.restart())
        r = []
    if i == 'X':
        break
    if len(r) != 0:
        print("'"+j+"' ->", r)
    index += 1