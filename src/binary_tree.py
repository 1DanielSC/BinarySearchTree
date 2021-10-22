from node import Node
from collections import deque


#Methods to implement:
    #1 - isBalanced()


class BinaryTree:
    def __init__(self, keyElement):
        self.root = Node(int(keyElement))
        self.size = 1



    def getSize(self):
        return int(self.size)

    

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
    





    def isBinarySearchTree(self):
        if(self.root == None):
            return False
        return self.__isBinarySearchTree(self.root,None,None)
    
    def __isBinarySearchTree(self,root,rootMin,rootMax):
        if(root == None):
            return True
        if(rootMin != None and root.key < rootMin.key):
            return False
        if(rootMax != None and root.key > rootMax.key):
            return False
        return self.__isBinarySearchTree(root.left,rootMin,root) and self.__isBinarySearchTree(root.right,root,rootMax)





#To return a number that represents an unsuccessful operation, we can return "None" so as to avoid retrieving a negative number

#Kth Element according to irOrder traversal
    def findKthElement(self, position):
        if(int(position) < 0):
            print("Invalid position: Less than 0")
            return

        elif(self.root.quantityLeft + self.root.quantityRight + 1 < int(position)):
            print("Error: Number of elements less than " + str(position))
            return

        else:
            element = self.__findKthElement(self.root,int(position))
            print("Element at position " + str(position) + ": " + str(element.key))



    def __findKthElement(self,root,position):
        if(root == None):
            print("There isn't element at this position.")
            return
        

        if(root.quantityLeft + 1 == position):
            return root
        elif(root.quantityLeft + 1 < position):
            return self.__findKthElement(root.right,position - (root.quantityLeft + 1))
        else:
            return self.__findKthElement(root.left,position)

    """
    def getSize(self):
        if self.root == None:
            return 0
        else: 
            return self.__getSize(self.root)

    def __getSize(self, root):
        if(root == None):
            return 0
        x = self.__getSize(root.left)
        y = self.__getSize(root.right)

        return (x + y + 1)
    """        