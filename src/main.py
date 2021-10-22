#Importing the file BST.py
#import bst 
from bst import BinarySearchTree




def readInputFile():
    inputFile = open("input/instructions.txt","r")

    if(not inputFile.readable()):
        print("Error: The file 'instructions.txt' cannot be read.")
        inputFile.close()
        return

    i = 1

    for line in inputFile:
        #print(line.strip())
        line.strip()
            #By default, the strip() function will remove all white space characters—spaces, tabs, new lines.


        #print("Line " + str(i) + " : " + str(read_instruction(line)))
        instruction = read_instruction(line)
        executeInstruction(str(instruction[0]),instruction[1])


        i+=1

    inputFile.close()





#Function to get the necessary information from a file line
#The instruction is composed by a string (operation to perform) along with an optional number
    #LINE COMPOSITION: INTRUCTION + " " + NUMBER

def read_instruction(fileLine):

    delim = " "
    instruction = ""
    number = ""
    flag = False

    for character in fileLine:
        if(character == '\n'):
            break

        elif(character == delim):
           flag = True
           
        elif(not flag):
           instruction += character
        elif(flag):
            number += character


    if(len(number) == 0):
        return (instruction,None)
    else:
        return (instruction,int(number))







def executeInstruction(instruction, number, tree):

    match instruction:
        case "PRINT":
            tree.print()
        case "INSERT":
            tree.insert(int(number))
        case "REMOVE":
            tree.remove(int(number))
        case "SEARCH":
            tree.search(int(number))
        case "FindKthElement":
            tree.findKthElement(int(number))
        case "SIZE":
            tree.getSize()
        case "PREORDER":
            tree.preOrder()
        case "INORDER":
            tree.inOrder()
        case "POSTORDER":
            tree.postOrder()
        case "LEVELORDER":
            tree.levelOrder()
        case _:
            print("Error: Invalid instruction.")
        




def main():
    tree = BinarySearchTree(10)
    tree.insert(3)
    tree.insert(23)
    tree.preOrder()

    tree.search(int(23))
        
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


    tree.insert(-2)
    tree.print()
    tree.findKthElement(2)
    tree.findKthElement(4)
    




if __name__ == '__main__':
    
    #readInputFile()
    main()
