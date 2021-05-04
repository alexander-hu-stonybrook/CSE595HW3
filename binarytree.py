class BinaryTree:

    #may need to actually call it left/right
    left = None;
    right = None;

    def __init__(self, data=None):
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,data):
        self._data = data

    def add_leftchild(self,tree):
        t1 = type(tree.data)
        t2 = type(self.data)
        if t1 == t2:
            self.left = tree
        else:
            raise TypeError("Type mismatch between " + t2.__name__ + " and " + t1.__name__)

    def add_rightchild(self,tree):
        t1 = type(tree.data)
        t2 = type(self.data)
        if t1 == t2:
            self.right = tree
        else:
            raise TypeError("Type mismatch between " + t2.__name__ + " and " + t1.__name__)

    def __iter__(self):
        stack = []
        if self.data != None:
            yield self
        else:
            pass
        if self.right != None:
            if self.right.data != None:
                stack.append(self.right)
        if self.left != None:
            if self.left.data != None:
                stack.append(self.left)
        while len(stack) > 0:
            ntree = stack.pop()
            yield ntree
            if ntree.right != None:
                if ntree.right.data != None:
                    stack.append(ntree.right)
            if ntree.left != None:
                if ntree.left.data != None:
                    stack.append(ntree.left)

t1 = BinaryTree(0)
t1.add_leftchild(BinaryTree(5))
t2 = BinaryTree(10)
t2.add_rightchild(BinaryTree(23))
t1.add_rightchild(t2)

print(t1.data)
print((t1.left).data)
print(t1.left.data, t1.data)

t1 = BinaryTree(1)
t2 = BinaryTree(2)
t3 = BinaryTree(3)
t4 = BinaryTree(4)
t6 = BinaryTree(6)

t1.add_leftchild(t2)
t1.add_rightchild(t3)
t2.add_leftchild(t4)
t3.add_rightchild(t6)

for i in t1:
    print(i.data)

'''
t1 = BinaryTree(0)
t1.add_leftchild(BinaryTree(5))
t2 = BinaryTree(10)
t2.add_rightchild(BinaryTree("not an int"))
t1.add_rightchild(t2)
'''
