import sys
from collections import deque
class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def add(self,data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.add(data)
            else:
                return
        else:
            self.data = data
intLinkedList = deque()
while True:
    m = list(map(int,sys.stdin.readline().split()))
    if m[0] == 0:
        intLinkedList.appendleft(m[1])
    elif m[0] == 1:
        intLinkedList.append(m[1])
    elif m[0] == 2:
        if m[1] in intLinkedList:
            intLinkedList.insert(intLinkedList.index(m[1])+1,m[2])
        else:
            intLinkedList.appendleft(m[2])
    else:
        break
def demChieuCao(node):
    if node is None:
        return 0
    return max(demChieuCao(node.right) + 1, demChieuCao(node.left) +1)
Tree = node()
for x in intLinkedList:
    Tree.add(x)

print(demChieuCao(Tree))