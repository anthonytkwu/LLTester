class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self, node=None):
        self.headval = node

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def addNodeEnd(self, node):
        if self.headval == None:
            self.headval = node
            return
        tester = self.headval
        while tester.nextval != None:
            tester = tester.nextval
        tester.nextval = node
    
    def newName(self):
        pass

    
    


list = SLinkedList(Node("Mon"))
e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")


list.addNodeEnd(e2)
list.addNodeEnd(e3)

list.remove("Mon")

list.listprint()