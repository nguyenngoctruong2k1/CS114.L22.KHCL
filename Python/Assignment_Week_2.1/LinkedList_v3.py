from random import randrange
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #thêm vào cuối
    def addTail(self, data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    #thêm vào đầu 
    def addHead(self, data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def addAfter(self, x, data):
        q = self.head
        while q != None:
            if q.data == x:
                p = node(data)
                p.next = q.next
                q.next = p
                if self.tail == q:
                    self.tail = p
                return
            q = q.next
        self.addHead(data)

    def remoteHead(self):
        if self.head == None:
            return
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp = None

    def remoteFirst(self, data):
        if self.head == None:
            return

        i = self.head
        if i.data == data:
            self.remoteHead()
            return

        cur = i.next
        while cur != None:
            if cur.data == data:
                if cur == self.tail:
                    self.tail = i
                    i.next = None
                    cur = None
                    return

                i.next = cur.next
                cur = None
                return
            i = i.next
            cur = cur.next

    def remoteFull(self, data):
        if self.head == None:
            return
        
        i = self.head
        while i != None and i.data == data:
            self.remoteHead()
            i = self.head

        cur = i.next
        while cur != None:
            if cur.data == data:
                if cur == self.tail:
                    self.tail = i
                    i.next = None
                    return
                else:
                    i.next = cur.next
            else:
                i = i.next
            cur = i.next

    def array(self):
        a = []
        i = self.head
        while i != None:
            a.append(i.data)
            i = i.next
        return a

def HamSinh():
    arr = []
    arr.append(randrange(6))
    if arr[0] in [0,1,3,4]:
        arr.append(randrange(100))
    elif arr[0] == 2:
        arr.append(randrange(100))
        arr.append(randrange(100))
    return arr
lst1 = []
lst = linklist()
Info = HamSinh()
while Info[0] != 6: 
    if Info[0] == 0:
        lst1.insert(0,Info[1])
        lst.addHead(Info[1])
    elif Info[0] == 1:
        lst1.append(Info[1])
        lst.addTail(Info[1])
    elif Info[0] == 2:
        if Info[1] in lst1:
            lst1.insert(lst1.index(Info[1]) + 1, Info[2])
        else:
            lst1.insert(0,Info[2])
        lst.addAfter(Info[1], Info[2])
    elif Info[0] == 3:
        if Info[1] in lst1:
            lst1.remove(Info[1])
        lst.remoteFirst(Info[1])
    elif Info[0] == 4:
        while Info[1] in lst1:
            lst1.remove(Info[1])
        lst.remoteFull(Info[1])
    else:
        if len(lst1) > 0:
            lst1.pop(0)
        lst.remoteHead()
    if lst1!=lst.array():
        print(Info)
        exit()
    Info = HamSinh()
