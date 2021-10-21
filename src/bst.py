from node import Node
from binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):

    def __init__(self, firstElement):
        self.root = Node(int(firstElement))



    def search(self, keyElement):
        if(self.__search(self.root, int(keyElement))):
            print(str(keyElement)  + " found in BST")
        else:
            print(str(keyElement)  + " was not found in BST")



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
            print(str(keyElement) + " is already present in the BST")
            return False

        elif(root.key < keyElement):
            if(not root.hasRight()):
                root.right = Node(int(keyElement))
                root.quantityRight += 1
                return True
            else:
                if(self.__insert(root.right, keyElement)):
                    root.quantityRight += 1
        else:
            if(not root.hasLeft()):
                root.left = Node(int(keyElement))
                root.quantityLeft += 1
                return True
            else:
                if(self.__insert(root.left, keyElement)):
                    root.quantityLeft += 1

        return False




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

            if(self.__remove(root.left,root,keyElement)):
                root.quantityLeft -= 1
            else:
                return False


        elif(root.key < keyElement):
            if(self.__remove(root.right,root,keyElement)):
                root.quantityRight -= 1
            else:
                return False

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

                if(self.__remove(root.right,successor)):
                    root.quantityRight -= 1
                else:
                    return False
        
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

