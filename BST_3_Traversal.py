class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BT:
    def __init__(self,value):
        self.root=Node(value)
        self.traversal = ""
    def print_tree(self,type):
        if type=="preorder":
            k=self.preorder_print(self.root)#整个结构都是以root为起始点的 所以root生万物
            return k
        elif type=="inorder":
            m=self.inorder_print(self.root,"")
            return m
        elif type=="postorder":
            n=self.postorder_print(self.root,"")
            return n

        else:
            return False


    def preorder_print(self,start):#注意我这个preorder和其他不一样 自己弄的很骄傲啊哈哈哈

        if start:

            self.traversal+=(str(start.value)+"-")
            self.traversal=self.preorder_print(start.left)
            self.traversal = self.preorder_print(start.right)
        return self.traversal

    def inorder_print(self,start,traversal):
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self,start,traversal):
        if start:
            traversal=self.postorder_print(start.left,traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

tree = BT(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))


