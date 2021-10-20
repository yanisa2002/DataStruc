ls = [e for e in input("Enter data to stack : ").split()]
print(ls)

# Doubly linked list-----------------------------
 
# def pushback(self,data):
#         newNode = Node(data)
#         newNode.prev,newNode.next = self.Dummytail.prev,self.Dummytail
#         self.Dummytail.prev.next = self.Dummytail.prev = newNode
#         self.size += 1

#  def pushfront(self,data):                                
#         newNode = Node(data)
#         newNode.next,newNode.prev = self.Dummyhead.next,self.Dummyhead
#         self.Dummyhead.next.prev = self.Dummyhead.next = newNode
#         self.size += 1

# def indexOf(self,data) :
#         current = self.Dummyhead.next
#         for i in range(self.size) :
#             if current.value == data :
#                 return i
#             current = current.next
#         return -1

#    def nodeAt(self,i) :
#         current = self.Dummyhead.next
#         for j in range(0,i) :
#             current = current.next
#         return current

# def insert(self, pos, data):
#         if int(pos) == 0 or self.size+int(pos) <= 0:
#             self.pushfront(data)
#         elif int(pos) >= self.size:
#             self.pushback(data)
#         else:
#             if pos < 0:
#                 self.insertBefore(self.nodeAt(self.size - abs(pos)),data)
#             else:
#                 self.insertBefore(self.nodeAt(pos),data)

#  def insertBefore(self,node,data) :
#         p = node.prev
#         newNode = Node(data)
#         newNode.prev,newNode.next = p,node
#         p.next = node.prev = newNode
#         self.size += 1

# def pop(self,i = None):
#         if i is None:
#             if self.size > 0:
#                 temp = self.Dummytail.prev
#                 Value = temp.value
#                 self.Dummytail.prev.prev.next = self.Dummytail
#                 self.Dummytail.prev = self.Dummytail.prev.prev
#                 temp.prev = temp.next = None
#                 self.size -= 1
#                 return Value
#         elif i < self.size and i >= 0:
#             nodePop = self.nodeAt(i)
#             Value = nodePop.value
#             nodePop.prev.next = nodePop.next
#             nodePop.next.prev = nodePop.prev 
#             nodePop.prev = nodePop.next = None
#             self.size -= 1
#             return Value
#         else: return "Out of index"

#   def remove(self,data):
#         self.pop(self.indexOf(data))
#---------------------------------------------

#-----------stack------------------
# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self,i):
#         self.items.append(i)

#     def pop(self):
#         return self.items.pop()
    
#     def isEmpty(self):
#         return len(self.items) == 0

#     def size(self):
#         return len(self.items)

    # ----------------------------------
# class ColorCrush:
#     def __init__(self,item=None):
#         if item is not None:
#             self.item = item
#         else:
#             self.item = []
    
#     def push(self,data):
#         self.item.append(data)
    
#     def pop(self):
#         return self.item.pop(0)

#     def peek(self):
#         return self.item[-1]
    
#     def size(self):
#         return len(self.item)

#     def isEmpty(self):
#         return self.item == []

# def same(x,y,z):
#     return x == y == z

#------------------------------------------------

# ------------Queue-----------------------------------
# class Queue:
#     def __init__(self):
#         self.items = []
    
#     def enQ(self,data):
#         self.items.append(data)
    
#     def deQ(self):
#         return self.items.pop(0)
    
#     def isEmpty(self):
#         return self.items == []
    
#     def size(self):
#         return len(self.items)
    # ---------------------------------------------------
# class Queue:
#     def __init__(self):
#         self.List = []
    
#     def enQ(self,x):
#         self.List.append(x)
    
#     def deQ(self):
#         return self.List.pop(0)
    
#     def rear(self):
#         return self.List[-1]
    
#     def front(self):
#         return self.List[0]
    
#     def isEmpty(self):
#         return self.List == []
    
#     def size(self):
#         return len(self.List)
    # ---------------------------------------------------   
# class ColorCrush:
#     def __init__(self,item=None):
#         if item is not None:
#             self.item = item
#         else:
#             self.item = []
    
#     def push(self,data):
#         self.item.append(data)
    
#     def pop(self):
#         return self.item.pop(0)

#     def peek(self):
#         return self.item[-1]
    
#     def size(self):
#         return len(self.item)

#     def isEmpty(self):
#         return self.item == []

# def same(x,y,z):
#     return x == y == z
# ---------------------------------------------------