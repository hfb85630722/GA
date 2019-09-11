class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):#我头想炸了才想明白这个是in order traversal。这个函数里面实际上有三块程序：if, print, if.  if---if----if
                                                                                 # p    p     p
        if self.left:                                                           # if   if    if
            self.left.PrintTree()                                                #12   6     3  3这个node输出来之后返回的是上一个的if，表示上一个的if这一行执行成功
                                                                                      #所以返回到上一层的if，表示完成，接着执行下一行就是输出6，以此类推。
        print(self.data)
        if self.right:
            self.right.PrintTree()


# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()