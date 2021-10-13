from node import Node
from collections import deque


class BinarySearchTree:

    def __init__(self, firstElement):
        self.root = Node(int(firstElement))


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


    def search(self, keyElement):
        return self.__search(self.root, int(keyElement))


    def __search(self, root, keyElement):
        if(root == None):
            return False
        if(root.key == keyElement):
            return True
        elif(root.key > keyElement):
            return self.__search(root.left, keyElement)
        else:
            return self.__search(root.right, keyElement)

    



    def insert(self, keyElement):
        if(self.root == None):
            self.root = Node(int(keyElement))
        else:
            self.__insert(self.root,keyElement)


    def __insert(self, root, keyElement):
        if(root.key == keyElement):
            return
        elif(root.key < keyElement):
            if(not root.hasRight()):
                root.right = Node(int(keyElement))
            else:
                return self.__insert(root.right, keyElement)
        else:
            if(not root.hasLeft()):
                root.left = Node(int(keyElement))
            else:
                return self.__insert(root.left, keyElement)


    def remove(self,keyElement):
        if(self.root == None):
            print("The tree is empty")
            return False
        return self.__remove(self.root, None, int(keyElement))




    def __remove(self,root,parent,keyElement):
        if(self.root == None):
            print(str(keyElement) + " was not found")
            return False

        if(root.key > keyElement):
            return self.__remove(root.left,root,keyElement)


        elif(root.key < keyElement):
            return self.__remove(root.right,root,keyElement)

        else:
            if(root.isChild()):

                if(parent.left.key == root.key):
                    parent.left = None
                else:
                    parent.right = None

            elif(not root.hasRight()):
                if(parent.left.key == root.key):
                    parent.left = root.left
                else:
                    parent.right = root.left
            
            elif(not root.hasLeft()):
                if(parent.left.key == root.key):
                    parent.left = root.right
                else:
                    parent.right = root.right

            else:
                successor = self.__findSuccessor(root,keyElement)
                root.key = int(successor)
                self.__remove(root.right,successor)
        
        return True

    def __findSuccessor(self,root,keyElement):

        if(root.hasLeft()):
            return self.__findSuccessor(root.left,keyElement)
        else:
            return root.key



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