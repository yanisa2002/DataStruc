class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    dummy = Node(None)
    dummy.next = Node(LL[0])
    cur = dummy.next
    for i in LL[1:]:
        cur.next = Node(i)
        cur = cur.next
    cur.next = None
    return dummy.next

def printLL(head):
    cur = head
    string = str(head.value) + " "
    while cur.next is not None:
        string += str(cur.next.value) + " "
        cur = cur.next
    return string

def SIZE(head):
    cur = head
    count = 0
    while cur:
        count += 1
        cur = cur.next
    return count

def bottomUp(head, n):
    cur = head
    for i in range(1,n):
        cur = cur.next
    head2 = cur.next
    cur.next = None
    return head,head2

def lift(head1, head2):
    cur = head1
    while cur.next:
        cur = cur.next
    cur.next = head2
    return head1

def riffleShuffle(head1, head2):
    dummy = Node(None)
    cur = dummy
    while True:
        if head1 is None:
            cur.next = head2
            break
        if head2 is None:
            cur.next = head1
            break
        cur.next = head1
        head1 = head1.next
        cur = cur.next
        cur.next = head2
        head2 = head2.next
        cur = cur.next
    return dummy.next

def deRiffle(LL, n):
    LEN = SIZE(LL)
    dummy1 = Node(None)
    dummy2 = Node(None)
    c1 = dummy1
    c2 = dummy2
    cur = LL
    while True:
        if SIZE(dummy1.next) == n:
            c2.next = cur
            break
        if SIZE(dummy2.next) == LEN-n:
            c1.next = cur
            break
        c1.next = cur
        cur = cur.next
        c1 = c1.next
        c1.next = None
        c2.next = cur
        cur = cur.next
        c2 = c2.next
        c2.next = None 
    return dummy1.next,dummy2.next     

def scarmble(head, b, r, size):
    ls = size
    per_b = int(ls*(b/100))
    per_r = int(ls*(r/100))

    h1,h2 = bottomUp(head, per_b)
    print("BottomUp {:.3f} % : {}{}".format(b,printLL(h2),printLL(h1)))
    
    h1,h2 = bottomUp(lift(h2,h1), per_r)
    new = riffleShuffle(h1,h2)
    print("Riffle {:.3f} % : {}".format(r,printLL(new)))
    
    h1,h2 = deRiffle(new, per_r)
    print("Deriffle {:.3f} % : {}{}".format(r,printLL(h1),printLL(h2)))
    
    h1,h2 = bottomUp(lift(h1, h2), ls-per_b)
    lsStart = lift(h2,h1)
    print("Debottomup {:.3f} % : {}".format(b,printLL(lsStart)))

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)