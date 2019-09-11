class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right = None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        if data<cur_node.data:#这里可以用 .data的形式是因为当你用到这个函数的时候 它本身（cur_node)已经就是个node了
            if cur_node.left==None:
                cur_node.left=Node(data)
            else:
                self._insert(data,cur_node.left)

        elif data>cur_node.data:
            if cur_node.right==None:
                cur_node.right=Node(data)
            else:
                self._insert(data,cur_node.right)

        else:
            print("Value is already in the tree!")

    def find(self,data):
        if self.root:
            is_found=self._find(data,self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self,data,cur_node):

        if data>cur_node.data and cur_node.right:
             return self._find(data,cur_node.right)#45，47 行必须得加return 否则检查了root node之后 再检查下面 永远没有一个返回 所以即使你想找的在下面藏着，也只能返回None，所以结果就是 False 不信的话可以试一试
        elif data<cur_node.data and cur_node.left:
             return self._find(data,cur_node.left)
        if data==cur_node.data:
            return True


a=BST()
a.insert(1)
a.insert(2)
print(a.find(2))
























