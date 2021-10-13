class Node:
    def __init__(self, keyValue):
        self.key = int(keyValue)
        self.left = None
        self.right = None
    
    

    def isChild(self):
        if(self.left == None and self.right == None):
            return True
        else: return False
    
    def hasLeft(self):
        if self.left == None :
            return False
        else: return True

    def hasRight(self):
        if self.right == None :
            return False
        else: return True

