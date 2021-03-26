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
    

def countNodeLa(node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        return countNodeLa(node.right) + countNodeLa(node.left)


root = node()
while True:
    m = int(input())
    if m == 0:
        break
    root.add(m)

print(countNodeLa(root))