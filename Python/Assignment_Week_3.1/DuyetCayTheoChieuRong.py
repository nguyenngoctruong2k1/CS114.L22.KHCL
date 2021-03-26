import sys 
class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def add(self,data):
        if self.data:
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
            self.data = data
    

def printNode(node):
    if node is None:
        return
    queue = []
    queue.append(node)
    while (len(queue) > 0):
        current = queue.pop(0)
        print(current.data, end = ' ')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

root = node()
while True:
    m = int(input())
    if m == 0:
        break
    root.add(m)

printNode(root)


