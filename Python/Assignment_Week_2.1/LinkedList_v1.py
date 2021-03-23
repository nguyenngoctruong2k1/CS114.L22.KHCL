import sys 
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
        i = self.head
        while i != None and i.data == data:
            self.remoteHead()
            i = self.head
        if self.head == None:
            return
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

    def print(self):
        if self.head == None:
            print('blank', end = ' ')
        i = self.head
        while i != None:
            print(i.data, end = ' ')
            i = i.next
        print()

lst = linklist()
Info = sys.stdin.readline().split()
while Info[0] != '6': 
    if Info[0] == '0':
        lst.addHead(Info[1])
    elif Info[0] == '1':
        lst.addTail(Info[1])
    elif Info[0] == '2':
        lst.addAfter(Info[1], Info[2])
    elif Info[0] == '3':
        lst.remoteFirst(Info[1])
    elif Info[0] == '4':
        lst.remoteFull(Info[1])
    else:
        lst.remoteHead()
    Info = sys.stdin.readline().split()
    
lst.print()