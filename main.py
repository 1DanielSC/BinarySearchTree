#Importing the file BST.py
#import bst 
from bst import BinarySearchTree


def main():
    tree = BinarySearchTree(10)
    tree.insert(3)
    tree.insert(23)
    tree.preOrder()

    if(tree.search(int(23))):
        print("Value of 23 found in BST")
    else:
        print("Value of 23 not found in BST")

    print("Tree's size is: " + str(tree.getSize()))

    if(tree.remove(23)):
        print("Value of 23 was removed from BST")
    else:
        print("Value of 23 was not removed from BST")

    tree.insert(0)
    tree.insert(60)

    tree.levelOrder()

    tree.remove(3)
    tree.levelOrder()


if __name__ == '__main__':
    main()