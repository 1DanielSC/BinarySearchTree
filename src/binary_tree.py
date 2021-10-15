from node import Node
from collections import deque


class BinaryTree:
    def __init__(self, keyElement):
        self.root = Node(int(keyElement))
    

    def preOrder(self):
        print("Pre-Order traversal: ",end='')
        self.__preOrder(self.root)
        print("")

    def __preOrder(self, root):
        if(root == None):
            return

        print(str(root.key) + " ",end='')
        self.__preOrder(root.left)
        self.__preOrder(root.right)





    def inOrder(self):
        print("In-Order traversal: ",end='')
        self.__inOrder(self.root)
        print("")

    def __inOrder(self,root):
        if(root == None):
            return
        self.__inOrder(root.left)
        print(str(self.key),end='')
        self.__inOrder(root.right)





    def postOrder(self):
        print("Post Order traversal: ",end='')
        self.__postOrder(self.root)
        print("")

    def __postOrder(self,root):
        if(root == None):
            return
        self.__postOrder(root.left)
        self.__postOrder(root.right)
        print(str(root.key) + " ", end='')





    def print(self):
        if(self.root == None):
            print("Tree is empty")
        else:
            self.__print(self.root,int(0),"")
    
    def __print(self,root,level,tab):
        if(root == None):
            return
        
        self.__print(root.right,level + 1, tab + "\t")
        print(tab + "Level " + str(level) + " : " + str(root.key))
        self.__print(root.left,level + 1, tab + "\t")






    def levelOrder(self):
        if(self.root == None):
            return
        else:
            self.__levelOrder(self.root)
            print("")

    def __levelOrder(self,root):

        queue = deque()
        queue.append(root)

        print("Level order: ", end ='')

        while(len(queue) > 0):
            element = queue.popleft()
            print(str(element.key) + " ", end = '')

            if(element.hasLeft()):
                queue.append(element.left)

            if(element.hasRight()):
                queue.append(element.right)

        return