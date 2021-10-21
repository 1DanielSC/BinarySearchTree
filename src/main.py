#Importing the file BST.py
#import bst 
from bst import BinarySearchTree



#Features to implement later on

    #Note 2: Create an Application class to run the program properly

    #Note 3: Read an input file consisting of ordered operations that the program must follow
            #Implement a function that identifies the instruction and call the proper method
            #Compute one instruction at a time

    #Note 4: AVL tree (new class)




def fileOP():
    inputFile = open("instructions.txt","r")

    if(not inputFile.readable()):
        print("Error: The file 'instructions.txt' cannot be read.")
        inputFile.close()
        return

    i = 1

    for line in inputFile:
        #print(line.strip())
        line.strip()
            #By default, the strip() function will remove all white space characters—spaces, tabs, new lines.
        print("Line " + str(i) + " : " + str(read_instruction(line)))
        i+=1

    inputFile.close()



    outputFile = open("end.txt","w")

    if(outputFile.writable()):
        stringd = input("Type sth that you want to see in the file: ")
        outputFile.write(stringd)
    else:
        print("Error: Cannot write in file.")

    outputFile.close()






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
        return instruction
    else:
        return (instruction,int(number))






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
    




if __name__ == '__main__':
    main()
    #fileOP()
