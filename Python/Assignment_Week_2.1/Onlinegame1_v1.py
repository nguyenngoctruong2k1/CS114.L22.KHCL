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
    
    def search(self,data):
        if self.data None:
            return False
        else:
            if data < self.data:
                if self.left is None:
                    return False
                else:
                    return self.left.search(data)
            elif data == self.data:
                return True
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.search(data)

root = node()
m = sys.stdin.readline().split()
result = ""
while m[0] != '0':
    if m[0] == '1':
        root.add(int(m[1]))
    elif root.search(int(m[1])):
        result += "1\n"
    else:
        result += "0\n"
    m = sys.stdin.readline().split()
print(result)